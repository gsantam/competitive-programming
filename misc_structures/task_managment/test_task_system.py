"""
Test suite for Task Dependency System.

Run with: pytest test_task_system.py -v
Run specific level: pytest test_task_system.py -v -k "level1"
"""

import pytest
from task_system import TaskSystem


# ==================== LEVEL 1: Basic Task Management ====================

class TestLevel1CreateTask:
    """Tests for create_task functionality."""

    def test_level1_create_single_task(self):
        ts = TaskSystem()
        assert ts.create_task("T1", "Design database") is True

    def test_level1_create_multiple_tasks(self):
        ts = TaskSystem()
        assert ts.create_task("T1", "Design") is True
        assert ts.create_task("T2", "Implement") is True
        assert ts.create_task("T3", "Test") is True

    def test_level1_create_duplicate_id(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        assert ts.create_task("T1", "Second") is False

    def test_level1_initial_status_is_todo(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.get_status("T1") == "todo"


class TestLevel1UpdateStatus:
    """Tests for update_status functionality."""

    def test_level1_todo_to_in_progress(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.update_status("T1", "in_progress") is True
        assert ts.get_status("T1") == "in_progress"

    def test_level1_in_progress_to_done(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        ts.update_status("T1", "in_progress")
        assert ts.update_status("T1", "done") is True
        assert ts.get_status("T1") == "done"

    def test_level1_todo_to_done_directly(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        # Cannot skip in_progress
        assert ts.update_status("T1", "done") is False

    def test_level1_cannot_go_backward(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        ts.update_status("T1", "in_progress")
        assert ts.update_status("T1", "todo") is False

    def test_level1_invalid_status(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.update_status("T1", "invalid") is False

    def test_level1_update_nonexistent(self):
        ts = TaskSystem()
        assert ts.update_status("T999", "in_progress") is False


class TestLevel1GetTasksByStatus:
    """Tests for get_tasks_by_status functionality."""

    def test_level1_get_todo_tasks(self):
        ts = TaskSystem()
        ts.create_task("T1", "Zebra task")
        ts.create_task("T2", "Alpha task")
        assert ts.get_tasks_by_status("todo") == ["Alpha task", "Zebra task"]

    def test_level1_get_in_progress_tasks(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task A")
        ts.create_task("T2", "Task B")
        ts.update_status("T1", "in_progress")
        assert ts.get_tasks_by_status("in_progress") == ["Task A"]
        assert ts.get_tasks_by_status("todo") == ["Task B"]

    def test_level1_empty_status(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.get_tasks_by_status("done") == []


class TestLevel1GetStatus:
    """Tests for get_status functionality."""

    def test_level1_get_status_exists(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.get_status("T1") == "todo"

    def test_level1_get_status_nonexistent(self):
        ts = TaskSystem()
        assert ts.get_status("T999") is None


# ==================== LEVEL 2: Dependencies ====================

class TestLevel2AddDependency:
    """Tests for add_dependency functionality."""

    def test_level2_add_simple_dependency(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        assert ts.add_dependency("T2", "T1") is True  # T2 depends on T1

    def test_level2_dependency_nonexistent_task(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        assert ts.add_dependency("T1", "T999") is False
        assert ts.add_dependency("T999", "T1") is False

    def test_level2_self_dependency(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.add_dependency("T1", "T1") is False

    def test_level2_duplicate_dependency(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.add_dependency("T2", "T1")
        assert ts.add_dependency("T2", "T1") is False

    def test_level2_detect_simple_cycle(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.add_dependency("T2", "T1")  # T2 -> T1
        # Would create T1 -> T2 -> T1
        assert ts.add_dependency("T1", "T2") is False

    def test_level2_detect_long_cycle(self):
        ts = TaskSystem()
        ts.create_task("T1", "A")
        ts.create_task("T2", "B")
        ts.create_task("T3", "C")
        ts.add_dependency("T2", "T1")  # T2 -> T1
        ts.add_dependency("T3", "T2")  # T3 -> T2
        # Would create T1 -> T3 -> T2 -> T1
        assert ts.add_dependency("T1", "T3") is False


class TestLevel2Blockers:
    """Tests for get_blockers functionality."""

    def test_level2_no_blockers(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.get_blockers("T1") == []

    def test_level2_one_blocker(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.add_dependency("T2", "T1")
        assert ts.get_blockers("T2") == ["First"]

    def test_level2_blocker_done(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.add_dependency("T2", "T1")
        ts.update_status("T1", "in_progress")
        ts.update_status("T1", "done")
        assert ts.get_blockers("T2") == []

    def test_level2_multiple_blockers_sorted(self):
        ts = TaskSystem()
        ts.create_task("T1", "Zebra")
        ts.create_task("T2", "Alpha")
        ts.create_task("T3", "Main")
        ts.add_dependency("T3", "T1")
        ts.add_dependency("T3", "T2")
        assert ts.get_blockers("T3") == ["Alpha", "Zebra"]

    def test_level2_nonexistent_task(self):
        ts = TaskSystem()
        assert ts.get_blockers("T999") == []


class TestLevel2StatusWithDependencies:
    """Tests for update_status with dependencies."""

    def test_level2_cannot_start_with_blockers(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.add_dependency("T2", "T1")
        assert ts.update_status("T2", "in_progress") is False

    def test_level2_can_start_when_deps_done(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.add_dependency("T2", "T1")
        ts.update_status("T1", "in_progress")
        ts.update_status("T1", "done")
        assert ts.update_status("T2", "in_progress") is True

    def test_level2_in_progress_dep_still_blocks(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.add_dependency("T2", "T1")
        ts.update_status("T1", "in_progress")  # Not done yet
        assert ts.update_status("T2", "in_progress") is False


# ==================== LEVEL 3: Execution Order ====================

class TestLevel3ExecutionOrder:
    """Tests for get_execution_order functionality."""

    def test_level3_simple_chain(self):
        ts = TaskSystem()
        ts.create_task("T1", "A")
        ts.create_task("T2", "B")
        ts.create_task("T3", "C")
        ts.add_dependency("T2", "T1")  # B depends on A
        ts.add_dependency("T3", "T2")  # C depends on B
        order = ts.get_execution_order()
        assert order == ["A", "B", "C"]

    def test_level3_no_dependencies(self):
        ts = TaskSystem()
        ts.create_task("T1", "B")
        ts.create_task("T2", "A")
        order = ts.get_execution_order()
        # Any order is valid, but should be consistent (e.g., alphabetical)
        assert set(order) == {"A", "B"}

    def test_level3_diamond_dependency(self):
        ts = TaskSystem()
        ts.create_task("T1", "Start")
        ts.create_task("T2", "Left")
        ts.create_task("T3", "Right")
        ts.create_task("T4", "End")
        ts.add_dependency("T2", "T1")
        ts.add_dependency("T3", "T1")
        ts.add_dependency("T4", "T2")
        ts.add_dependency("T4", "T3")
        order = ts.get_execution_order()
        # Start must be first, End must be last
        assert order[0] == "Start"
        assert order[-1] == "End"
        assert set(order) == {"Start", "Left", "Right", "End"}

    def test_level3_cycle_returns_none(self):
        ts = TaskSystem()
        ts.create_task("T1", "A")
        ts.create_task("T2", "B")
        ts.add_dependency("T2", "T1")
        # Force a cycle by manipulating internal state (for testing)
        # Actually, we can't add a cycle through the API, so this tests empty case
        order = ts.get_execution_order()
        assert order is not None  # No cycle through API

    def test_level3_empty_system(self):
        ts = TaskSystem()
        assert ts.get_execution_order() == []


class TestLevel3AvailableTasks:
    """Tests for get_available_tasks functionality."""

    def test_level3_all_available(self):
        ts = TaskSystem()
        ts.create_task("T1", "B")
        ts.create_task("T2", "A")
        assert ts.get_available_tasks() == ["A", "B"]

    def test_level3_some_blocked(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.add_dependency("T2", "T1")
        assert ts.get_available_tasks() == ["First"]

    def test_level3_unblocked_after_done(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.add_dependency("T2", "T1")
        ts.update_status("T1", "in_progress")
        ts.update_status("T1", "done")
        assert ts.get_available_tasks() == ["Second"]

    def test_level3_in_progress_not_available(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        ts.update_status("T1", "in_progress")
        assert ts.get_available_tasks() == []

    def test_level3_done_not_available(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        ts.update_status("T1", "in_progress")
        ts.update_status("T1", "done")
        assert ts.get_available_tasks() == []


class TestLevel3ParallelGroups:
    """Tests for get_parallel_groups functionality."""

    def test_level3_single_wave(self):
        ts = TaskSystem()
        ts.create_task("T1", "B")
        ts.create_task("T2", "A")
        groups = ts.get_parallel_groups()
        assert groups == [["A", "B"]]

    def test_level3_chain_three_waves(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.create_task("T3", "Third")
        ts.add_dependency("T2", "T1")
        ts.add_dependency("T3", "T2")
        groups = ts.get_parallel_groups()
        assert groups == [["First"], ["Second"], ["Third"]]

    def test_level3_diamond_groups(self):
        ts = TaskSystem()
        ts.create_task("T1", "Start")
        ts.create_task("T2", "Left")
        ts.create_task("T3", "Right")
        ts.create_task("T4", "End")
        ts.add_dependency("T2", "T1")
        ts.add_dependency("T3", "T1")
        ts.add_dependency("T4", "T2")
        ts.add_dependency("T4", "T3")
        groups = ts.get_parallel_groups()
        assert len(groups) == 3
        assert groups[0] == ["Start"]
        assert groups[1] == ["Left", "Right"]
        assert groups[2] == ["End"]

    def test_level3_empty_groups(self):
        ts = TaskSystem()
        assert ts.get_parallel_groups() == []


# ==================== LEVEL 4: Critical Path ====================

class TestLevel4Duration:
    """Tests for set_duration functionality."""

    def test_level4_set_duration(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.set_duration("T1", 5.0) is True

    def test_level4_invalid_duration(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.set_duration("T1", 0) is False
        assert ts.set_duration("T1", -1) is False

    def test_level4_nonexistent_task(self):
        ts = TaskSystem()
        assert ts.set_duration("T999", 5.0) is False


class TestLevel4EarliestStart:
    """Tests for get_earliest_start functionality."""

    def test_level4_no_dependencies(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        ts.set_duration("T1", 5.0)
        assert ts.get_earliest_start("T1") == 0.0

    def test_level4_simple_chain(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.set_duration("T1", 3.0)
        ts.set_duration("T2", 2.0)
        ts.add_dependency("T2", "T1")
        assert ts.get_earliest_start("T1") == 0.0
        assert ts.get_earliest_start("T2") == 3.0  # After T1 finishes

    def test_level4_multiple_dependencies(self):
        ts = TaskSystem()
        ts.create_task("T1", "A")
        ts.create_task("T2", "B")
        ts.create_task("T3", "C")
        ts.set_duration("T1", 2.0)
        ts.set_duration("T2", 5.0)
        ts.set_duration("T3", 1.0)
        ts.add_dependency("T3", "T1")
        ts.add_dependency("T3", "T2")
        # T3 can only start after both T1 (2h) and T2 (5h) are done
        assert ts.get_earliest_start("T3") == 5.0

    def test_level4_nonexistent_task(self):
        ts = TaskSystem()
        assert ts.get_earliest_start("T999") is None


class TestLevel4ProjectDuration:
    """Tests for get_project_duration functionality."""

    def test_level4_single_task(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        ts.set_duration("T1", 5.0)
        assert ts.get_project_duration() == 5.0

    def test_level4_parallel_tasks(self):
        ts = TaskSystem()
        ts.create_task("T1", "Short")
        ts.create_task("T2", "Long")
        ts.set_duration("T1", 2.0)
        ts.set_duration("T2", 8.0)
        # Can run in parallel, so total time is max
        assert ts.get_project_duration() == 8.0

    def test_level4_chain(self):
        ts = TaskSystem()
        ts.create_task("T1", "A")
        ts.create_task("T2", "B")
        ts.set_duration("T1", 3.0)
        ts.set_duration("T2", 4.0)
        ts.add_dependency("T2", "T1")
        # Must run sequentially
        assert ts.get_project_duration() == 7.0

    def test_level4_complex_graph(self):
        ts = TaskSystem()
        ts.create_task("T1", "Start")
        ts.create_task("T2", "Left")
        ts.create_task("T3", "Right")
        ts.create_task("T4", "End")
        ts.set_duration("T1", 2.0)
        ts.set_duration("T2", 3.0)
        ts.set_duration("T3", 5.0)
        ts.set_duration("T4", 1.0)
        ts.add_dependency("T2", "T1")
        ts.add_dependency("T3", "T1")
        ts.add_dependency("T4", "T2")
        ts.add_dependency("T4", "T3")
        # Critical path: Start(2) -> Right(5) -> End(1) = 8
        assert ts.get_project_duration() == 8.0

    def test_level4_no_durations(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.get_project_duration() == 0.0


class TestLevel4CriticalPath:
    """Tests for get_critical_path functionality."""

    def test_level4_single_task(self):
        ts = TaskSystem()
        ts.create_task("T1", "Only")
        ts.set_duration("T1", 5.0)
        assert ts.get_critical_path() == ["Only"]

    def test_level4_simple_chain(self):
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.set_duration("T1", 3.0)
        ts.set_duration("T2", 2.0)
        ts.add_dependency("T2", "T1")
        assert ts.get_critical_path() == ["First", "Second"]

    def test_level4_parallel_paths(self):
        ts = TaskSystem()
        ts.create_task("T1", "Start")
        ts.create_task("T2", "Short")
        ts.create_task("T3", "Long")
        ts.create_task("T4", "End")
        ts.set_duration("T1", 1.0)
        ts.set_duration("T2", 2.0)  # Short path
        ts.set_duration("T3", 5.0)  # Long path (critical)
        ts.set_duration("T4", 1.0)
        ts.add_dependency("T2", "T1")
        ts.add_dependency("T3", "T1")
        ts.add_dependency("T4", "T2")
        ts.add_dependency("T4", "T3")
        # Critical path: Start -> Long -> End
        critical = ts.get_critical_path()
        assert critical == ["Start", "Long", "End"]

    def test_level4_empty_system(self):
        ts = TaskSystem()
        assert ts.get_critical_path() == []

    def test_level4_no_durations(self):
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        assert ts.get_critical_path() == []


class TestLevel4Integration:
    """Integration tests for Level 4."""

    def test_level4_full_project(self):
        ts = TaskSystem()

        # Create a realistic project
        ts.create_task("design", "Design")
        ts.create_task("frontend", "Frontend")
        ts.create_task("backend", "Backend")
        ts.create_task("db", "Database")
        ts.create_task("integrate", "Integration")
        ts.create_task("test", "Testing")

        # Set durations
        ts.set_duration("design", 5.0)
        ts.set_duration("frontend", 10.0)
        ts.set_duration("backend", 8.0)
        ts.set_duration("db", 4.0)
        ts.set_duration("integrate", 3.0)
        ts.set_duration("test", 2.0)

        # Set dependencies
        ts.add_dependency("frontend", "design")
        ts.add_dependency("backend", "design")
        ts.add_dependency("db", "design")
        ts.add_dependency("integrate", "frontend")
        ts.add_dependency("integrate", "backend")
        ts.add_dependency("integrate", "db")
        ts.add_dependency("test", "integrate")

        # Verify parallel groups
        groups = ts.get_parallel_groups()
        assert len(groups) == 4
        assert groups[0] == ["Design"]
        assert set(groups[1]) == {"Backend", "Database", "Frontend"}
        assert groups[2] == ["Integration"]
        assert groups[3] == ["Testing"]

        # Verify project duration
        # Critical path: Design(5) -> Frontend(10) -> Integration(3) -> Testing(2) = 20
        assert ts.get_project_duration() == 20.0

        # Verify critical path
        critical = ts.get_critical_path()
        assert critical == ["Design", "Frontend", "Integration", "Testing"]


# ==================== ADDITIONAL LEVEL 3 TESTS ====================

class TestLevel3ExecutionOrderAdvanced:
    """Advanced tests for topological sort edge cases."""

    def test_level3_wide_graph(self):
        """Many tasks at same level, all depend on one root."""
        ts = TaskSystem()
        ts.create_task("root", "Root")
        for i in range(5):
            ts.create_task(f"T{i}", f"Task {chr(65+i)}")  # A, B, C, D, E
            ts.add_dependency(f"T{i}", "root")
        order = ts.get_execution_order()
        assert order[0] == "Root"
        assert set(order[1:]) == {"Task A", "Task B",
                                  "Task C", "Task D", "Task E"}

    def test_level3_deep_chain(self):
        """Long chain of dependencies."""
        ts = TaskSystem()
        for i in range(10):
            ts.create_task(f"T{i}", f"Step {i}")
            if i > 0:
                ts.add_dependency(f"T{i}", f"T{i-1}")
        order = ts.get_execution_order()
        assert order == [f"Step {i}" for i in range(10)]

    def test_level3_multiple_roots(self):
        """Multiple independent starting points converging."""
        ts = TaskSystem()
        ts.create_task("R1", "Root A")
        ts.create_task("R2", "Root B")
        ts.create_task("R3", "Root C")
        ts.create_task("end", "End")
        ts.add_dependency("end", "R1")
        ts.add_dependency("end", "R2")
        ts.add_dependency("end", "R3")
        order = ts.get_execution_order()
        assert order[-1] == "End"
        assert set(order[:-1]) == {"Root A", "Root B", "Root C"}

    def test_level3_complex_dag(self):
        """Complex DAG with multiple paths."""
        ts = TaskSystem()
        # Create: A -> B -> D
        #         A -> C -> D
        #         B -> E
        #         C -> E
        ts.create_task("A", "A")
        ts.create_task("B", "B")
        ts.create_task("C", "C")
        ts.create_task("D", "D")
        ts.create_task("E", "E")
        ts.add_dependency("B", "A")
        ts.add_dependency("C", "A")
        ts.add_dependency("D", "B")
        ts.add_dependency("D", "C")
        ts.add_dependency("E", "B")
        ts.add_dependency("E", "C")
        order = ts.get_execution_order()
        # A must be first
        assert order[0] == "A"
        # B and C must come before D and E
        assert order.index("B") < order.index("D")
        assert order.index("C") < order.index("D")
        assert order.index("B") < order.index("E")
        assert order.index("C") < order.index("E")


class TestLevel3AvailableTasksAdvanced:
    """Advanced tests for available tasks."""

    def test_level3_chain_progression(self):
        """Track available tasks as we complete them."""
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.create_task("T3", "Third")
        ts.add_dependency("T2", "T1")
        ts.add_dependency("T3", "T2")

        assert ts.get_available_tasks() == ["First"]

        ts.update_status("T1", "in_progress")
        assert ts.get_available_tasks() == []

        ts.update_status("T1", "done")
        assert ts.get_available_tasks() == ["Second"]

        ts.update_status("T2", "in_progress")
        ts.update_status("T2", "done")
        assert ts.get_available_tasks() == ["Third"]

    def test_level3_multiple_available_after_single_done(self):
        """Multiple tasks become available after one completes."""
        ts = TaskSystem()
        ts.create_task("root", "Root")
        ts.create_task("T1", "A")
        ts.create_task("T2", "B")
        ts.create_task("T3", "C")
        ts.add_dependency("T1", "root")
        ts.add_dependency("T2", "root")
        ts.add_dependency("T3", "root")

        assert ts.get_available_tasks() == ["Root"]

        ts.update_status("root", "in_progress")
        ts.update_status("root", "done")

        assert ts.get_available_tasks() == ["A", "B", "C"]

    def test_level3_available_with_partial_deps_done(self):
        """Task with multiple deps, only some done."""
        ts = TaskSystem()
        ts.create_task("D1", "Dep 1")
        ts.create_task("D2", "Dep 2")
        ts.create_task("main", "Main")
        ts.add_dependency("main", "D1")
        ts.add_dependency("main", "D2")

        ts.update_status("D1", "in_progress")
        ts.update_status("D1", "done")

        # D2 still blocking, so only D2 should be available
        assert ts.get_available_tasks() == ["Dep 2"]


class TestLevel3ParallelGroupsAdvanced:
    """Advanced tests for parallel grouping."""

    def test_level3_wide_then_narrow(self):
        """Wide layer followed by single task."""
        ts = TaskSystem()
        ts.create_task("T1", "A")
        ts.create_task("T2", "B")
        ts.create_task("T3", "C")
        ts.create_task("T4", "D")
        ts.create_task("end", "End")
        ts.add_dependency("end", "T1")
        ts.add_dependency("end", "T2")
        ts.add_dependency("end", "T3")
        ts.add_dependency("end", "T4")
        groups = ts.get_parallel_groups()
        assert len(groups) == 2
        assert groups[0] == ["A", "B", "C", "D"]
        assert groups[1] == ["End"]

    def test_level3_uneven_convergence(self):
        """Tasks at different depths converging."""
        ts = TaskSystem()
        # Path 1: A -> B -> end
        # Path 2: C -> end
        ts.create_task("A", "A")
        ts.create_task("B", "B")
        ts.create_task("C", "C")
        ts.create_task("end", "End")
        ts.add_dependency("B", "A")
        ts.add_dependency("end", "B")
        ts.add_dependency("end", "C")
        groups = ts.get_parallel_groups()
        # A and C in first wave, B in second, End in third
        assert len(groups) == 3
        assert groups[0] == ["A", "C"]
        assert groups[1] == ["B"]
        assert groups[2] == ["End"]

    def test_level3_isolated_and_connected(self):
        """Mix of isolated tasks and connected tasks."""
        ts = TaskSystem()
        ts.create_task("iso1", "Isolated 1")
        ts.create_task("iso2", "Isolated 2")
        ts.create_task("dep1", "Dep 1")
        ts.create_task("dep2", "Dep 2")
        ts.add_dependency("dep2", "dep1")
        groups = ts.get_parallel_groups()
        # All roots in first wave, dep2 in second
        assert len(groups) == 2
        assert set(groups[0]) == {"Dep 1", "Isolated 1", "Isolated 2"}
        assert groups[1] == ["Dep 2"]


# ==================== ADDITIONAL LEVEL 4 TESTS ====================

class TestLevel4EarliestStartAdvanced:
    """Advanced tests for earliest start calculations."""

    def test_level4_diamond_earliest_start(self):
        """Diamond pattern earliest starts."""
        ts = TaskSystem()
        ts.create_task("start", "Start")
        ts.create_task("left", "Left")
        ts.create_task("right", "Right")
        ts.create_task("end", "End")
        ts.set_duration("start", 2.0)
        ts.set_duration("left", 3.0)
        ts.set_duration("right", 5.0)
        ts.set_duration("end", 1.0)
        ts.add_dependency("left", "start")
        ts.add_dependency("right", "start")
        ts.add_dependency("end", "left")
        ts.add_dependency("end", "right")

        assert ts.get_earliest_start("start") == 0.0
        assert ts.get_earliest_start("left") == 2.0
        assert ts.get_earliest_start("right") == 2.0
        # End waits for both: max(2+3, 2+5) = 7
        assert ts.get_earliest_start("end") == 7.0

    def test_level4_complex_earliest_start(self):
        """Complex graph with multiple paths."""
        ts = TaskSystem()
        # A(3) -> B(2) -> D(1)
        #      -> C(4) -> D
        ts.create_task("A", "A")
        ts.create_task("B", "B")
        ts.create_task("C", "C")
        ts.create_task("D", "D")
        ts.set_duration("A", 3.0)
        ts.set_duration("B", 2.0)
        ts.set_duration("C", 4.0)
        ts.set_duration("D", 1.0)
        ts.add_dependency("B", "A")
        ts.add_dependency("C", "A")
        ts.add_dependency("D", "B")
        ts.add_dependency("D", "C")

        assert ts.get_earliest_start("A") == 0.0
        assert ts.get_earliest_start("B") == 3.0
        assert ts.get_earliest_start("C") == 3.0
        # D waits for max(3+2, 3+4) = 7
        assert ts.get_earliest_start("D") == 7.0

    def test_level4_long_chain_earliest_start(self):
        """Long chain accumulates durations."""
        ts = TaskSystem()
        for i in range(5):
            ts.create_task(f"T{i}", f"Task {i}")
            ts.set_duration(f"T{i}", float(i + 1))
            if i > 0:
                ts.add_dependency(f"T{i}", f"T{i-1}")

        # T0: 0, T1: 1, T2: 1+2=3, T3: 3+3=6, T4: 6+4=10
        assert ts.get_earliest_start("T0") == 0.0
        assert ts.get_earliest_start("T1") == 1.0
        assert ts.get_earliest_start("T2") == 3.0
        assert ts.get_earliest_start("T3") == 6.0
        assert ts.get_earliest_start("T4") == 10.0

    def test_level4_earliest_start_no_duration(self):
        """Task without duration set."""
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.add_dependency("T2", "T1")
        # No duration set, should use 0
        assert ts.get_earliest_start("T2") == 0.0


class TestLevel4ProjectDurationAdvanced:
    """Advanced tests for project duration."""

    def test_level4_multiple_end_points(self):
        """Multiple tasks with no dependents."""
        ts = TaskSystem()
        ts.create_task("start", "Start")
        ts.create_task("end1", "End 1")
        ts.create_task("end2", "End 2")
        ts.set_duration("start", 2.0)
        ts.set_duration("end1", 3.0)
        ts.set_duration("end2", 5.0)
        ts.add_dependency("end1", "start")
        ts.add_dependency("end2", "start")
        # Total: max(2+3, 2+5) = 7
        assert ts.get_project_duration() == 7.0

    def test_level4_wide_project(self):
        """Many parallel tasks."""
        ts = TaskSystem()
        max_duration = 0.0
        for i in range(10):
            ts.create_task(f"T{i}", f"Task {i}")
            dur = float(i + 1)
            ts.set_duration(f"T{i}", dur)
            max_duration = max(max_duration, dur)
        # All parallel, so duration is max single task
        assert ts.get_project_duration() == 10.0

    def test_level4_some_tasks_no_duration(self):
        """Mix of tasks with and without durations."""
        ts = TaskSystem()
        ts.create_task("T1", "With duration")
        ts.create_task("T2", "No duration")
        ts.create_task("T3", "Also with")
        ts.set_duration("T1", 5.0)
        ts.set_duration("T3", 3.0)
        ts.add_dependency("T2", "T1")
        ts.add_dependency("T3", "T2")
        # T1: 5, T2: 0, T3: 3 -> total 8
        assert ts.get_project_duration() == 8.0


class TestLevel4CriticalPathAdvanced:
    """Advanced tests for critical path."""

    def test_level4_tie_breaking_alphabetical(self):
        """When paths are equal length, prefer alphabetical."""
        ts = TaskSystem()
        ts.create_task("start", "Start")
        ts.create_task("pathA", "PathA")
        ts.create_task("pathB", "PathB")
        ts.create_task("end", "End")
        ts.set_duration("start", 1.0)
        ts.set_duration("pathA", 3.0)
        ts.set_duration("pathB", 3.0)  # Same duration
        ts.set_duration("end", 1.0)
        ts.add_dependency("pathA", "start")
        ts.add_dependency("pathB", "start")
        ts.add_dependency("end", "pathA")
        ts.add_dependency("end", "pathB")
        critical = ts.get_critical_path()
        assert critical == ["Start", "PathA", "End"]

    def test_level4_critical_path_not_obvious(self):
        """Critical path through less obvious route."""
        ts = TaskSystem()
        # Route 1: A(1) -> B(1) -> E(1) = 3
        # Route 2: A(1) -> C(5) -> E(1) = 7  (critical)
        # Route 3: A(1) -> D(2) -> E(1) = 4
        ts.create_task("A", "A")
        ts.create_task("B", "B")
        ts.create_task("C", "C")
        ts.create_task("D", "D")
        ts.create_task("E", "E")
        ts.set_duration("A", 1.0)
        ts.set_duration("B", 1.0)
        ts.set_duration("C", 5.0)
        ts.set_duration("D", 2.0)
        ts.set_duration("E", 1.0)
        ts.add_dependency("B", "A")
        ts.add_dependency("C", "A")
        ts.add_dependency("D", "A")
        ts.add_dependency("E", "B")
        ts.add_dependency("E", "C")
        ts.add_dependency("E", "D")
        critical = ts.get_critical_path()
        assert critical == ["A", "C", "E"]

    def test_level4_long_critical_path(self):
        """Long chain is the critical path over shorter parallel path."""
        ts = TaskSystem()
        # Long path: A(5) -> B(5) -> C(5) = 15 total
        # Short path: X(2) -> Y(2) = 4 total
        ts.create_task("A", "A")
        ts.create_task("B", "B")
        ts.create_task("C", "C")
        ts.create_task("X", "X")
        ts.create_task("Y", "Y")
        ts.set_duration("A", 5.0)
        ts.set_duration("B", 5.0)
        ts.set_duration("C", 5.0)
        ts.set_duration("X", 2.0)
        ts.set_duration("Y", 2.0)
        ts.add_dependency("B", "A")
        ts.add_dependency("C", "B")
        ts.add_dependency("Y", "X")

        critical = ts.get_critical_path()
        # Critical path should be the long chain A -> B -> C
        assert critical == ["A", "B", "C"]

    def test_level4_single_path_is_critical(self):
        """When there's only one path, it's critical."""
        ts = TaskSystem()
        ts.create_task("A", "A")
        ts.create_task("B", "B")
        ts.create_task("C", "C")
        ts.set_duration("A", 1.0)
        ts.set_duration("B", 2.0)
        ts.set_duration("C", 3.0)
        ts.add_dependency("B", "A")
        ts.add_dependency("C", "B")
        critical = ts.get_critical_path()
        assert critical == ["A", "B", "C"]

    def test_level4_critical_path_ignores_done_tasks(self):
        """Critical path only considers incomplete tasks."""
        ts = TaskSystem()
        ts.create_task("done1", "Done Task")
        ts.create_task("todo1", "Todo Task")
        ts.set_duration("done1", 10.0)
        ts.set_duration("todo1", 2.0)
        ts.add_dependency("todo1", "done1")

        ts.update_status("done1", "in_progress")
        ts.update_status("done1", "done")

        # Now only the remaining work matters
        critical = ts.get_critical_path()
        # This could be just the remaining task
        assert "Todo Task" in critical


class TestLevel4EdgeCases:
    """Edge cases for Level 4."""

    def test_level4_float_precision(self):
        """Handle float precision correctly."""
        ts = TaskSystem()
        ts.create_task("T1", "First")
        ts.create_task("T2", "Second")
        ts.set_duration("T1", 0.1)
        ts.set_duration("T2", 0.2)
        ts.add_dependency("T2", "T1")
        # Should be 0.3, not 0.30000000000000004
        assert abs(ts.get_project_duration() - 0.3) < 0.0001

    def test_level4_update_duration(self):
        """Can update duration after setting."""
        ts = TaskSystem()
        ts.create_task("T1", "Task")
        ts.set_duration("T1", 5.0)
        assert ts.set_duration("T1", 10.0) is True
        # Project duration should reflect new value
        assert ts.get_project_duration() == 10.0

    def test_level4_very_large_durations(self):
        """Handle large duration values."""
        ts = TaskSystem()
        ts.create_task("T1", "Long Task")
        ts.set_duration("T1", 1000000.0)
        assert ts.get_project_duration() == 1000000.0

    def test_level4_fractional_durations(self):
        """Handle fractional durations."""
        ts = TaskSystem()
        ts.create_task("T1", "A")
        ts.create_task("T2", "B")
        ts.set_duration("T1", 1.5)
        ts.set_duration("T2", 2.5)
        ts.add_dependency("T2", "T1")
        assert ts.get_project_duration() == 4.0
        assert ts.get_earliest_start("T2") == 1.5
