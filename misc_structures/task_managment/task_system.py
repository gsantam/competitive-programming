"""
Task Dependency System

Implement the methods below to pass all tests across 4 levels.
See README.md for detailed requirements for each level.

Key Challenges:
- Level 2: Cycle detection in directed graph
- Level 3: Topological sort
- Level 4: Critical path algorithm
"""
from collections import defaultdict


class TaskSystem:
    """
    A task management system with dependencies, scheduling, and critical path analysis.
    """

    def __init__(self):
        """Initialize the task system."""
        self.tasks = {}
        self.status = {"todo": set(), "in_progress": set(), "done": set()}

    # ==================== LEVEL 1: Basic Task Management ====================

    def create_task(self, task_id: str, name: str) -> bool:
        """
        Create a new task.

        Args:
            task_id: Unique identifier for the task
            name: Name of the task

        Returns:
            True if created, False if task_id already exists
        """
        if task_id in self.tasks:
            return False
        self.tasks[task_id] = {"name": name,
                               "status": "todo", "depends_on": set(), 'eta': 0}
        self.status["todo"].add(task_id)
        return True

    def get_status(self, task_id: str) -> str:
        """
        Get the status of a task.

        Returns:
            Status string ("todo", "in_progress", "done") or None if not found
        """
        if task_id not in self.tasks:
            return None
        return self.tasks[task_id]["status"]

    def update_status(self, task_id: str, new_status: str) -> bool:
        """
        Update task status.

        Rules:
            - Valid statuses: "todo", "in_progress", "done"
            - Can only move forward: todo -> in_progress -> done
            - (Level 2+) Can't start unless all dependencies are done

        Returns:
            True if updated, False if invalid transition or task not found
        """
        if task_id not in self.tasks:
            return False

        if new_status not in ('in_progress', 'done'):
            return False
        old_status = self.tasks[task_id]["status"]
        if old_status == "todo":
            if new_status != "in_progress":
                return False
            if len(self.get_blockers(task_id)) != 0:
                return False

        if (old_status == "in_progress" and new_status != "done"):
            return False
        self.status[old_status].remove(task_id)
        self.status[new_status].add(task_id)
        self.tasks[task_id]["status"] = new_status
        return True

    def get_tasks_by_status(self, status: str) -> list:
        """
        Get all tasks with a given status.

        Returns:
            List of task names sorted alphabetically
        """
        return sorted([self.tasks[task_id]["name"] for task_id in self.status[status]])

    def is_cycle(self, task_id):
        stack = [(task_id, set())]
        while len(stack) != 0:
            current_task_id, current_cycle = stack.pop()
            dependendants = self.tasks[current_task_id]["depends_on"]
            current_cycle_copy = current_cycle.copy()
            current_cycle_copy.add(current_task_id)
            for dependant in dependendants:
                if dependant in current_cycle:
                    return True
                stack.append([dependant, current_cycle_copy])
        return False

        # ==================== LEVEL 2: Dependencies ====================

    def add_dependency(self, task_id: str, depends_on: str) -> bool:
        """
        Add a dependency: task_id depends on depends_on.

        Rules:
            - Both tasks must exist
            - Cannot create circular dependencies
            - Cannot add duplicate dependency

        Returns:
            True if added, False if invalid or would create cycle
        """
        if task_id not in self.tasks or depends_on not in self.tasks:
            return False
        if depends_on in self.tasks[task_id]["depends_on"] or (task_id == depends_on):
            return False
        self.tasks[task_id]["depends_on"].add(depends_on)
        if self.is_cycle(task_id):
            self.tasks[task_id]["depends_on"].remove(depends_on)
            return False
        return True

    def get_blockers(self, task_id: str) -> list:
        """
        Get tasks blocking this task (incomplete dependencies).

        Returns:
            List of task names that are dependencies and not "done", sorted alphabetically.
            Empty list if task not found or no blockers.
        """
        if task_id not in self.tasks:
            return []
        stack = [task_id]
        blockers = set()
        while len(stack) != 0:
            current_task_id = stack.pop()
            dependendants = self.tasks[current_task_id]["depends_on"]
            for dependant in dependendants:
                if self.tasks[dependant]["status"] != 'done':
                    blockers.add(dependant)
        return sorted([self.tasks[task_id]["name"] for task_id in blockers])

    # ==================== LEVEL 3: Execution Order ====================

    def get_execution_order_helper(self) -> list:
        """
        Get a valid execution order for all tasks (topological sort).

        Returns:
            List of task names in valid execution order.
            None if there's a cycle (impossible to complete).
        """
        execution_order = []

        tasks_to_complete = {task_id: len(self.tasks[task_id]["depends_on"])
                             for task_id in self.tasks}
        current_tasks = [
            task_id for task_id in tasks_to_complete if tasks_to_complete[task_id] == 0]
        tasks_dependent_on_me = defaultdict(lambda: [])
        for task_id in self.tasks:
            for dependendices in self.tasks[task_id]["depends_on"]:
                tasks_dependent_on_me[dependendices].append(task_id)
        wave = {task_id: 0 for task_id in current_tasks}
        earliest_start = {task_id: 0 for task_id in current_tasks}

        while len(current_tasks) != 0:
            current_task = current_tasks.pop()
            execution_order.append(current_task)
            for task_dependent_on_me in tasks_dependent_on_me[current_task]:
                tasks_to_complete[task_dependent_on_me] -= 1
                if task_dependent_on_me not in wave:
                    wave[task_dependent_on_me] = wave[current_task]+1
                else:
                    wave[task_dependent_on_me] = max(
                        wave[current_task]+1, wave[task_dependent_on_me])
                if task_dependent_on_me not in earliest_start:
                    earliest_start[task_dependent_on_me] = earliest_start[current_task] + \
                        self.tasks[current_task]['eta']
                else:
                    earliest_start[task_dependent_on_me] = max(
                        earliest_start[current_task] +
                        self.tasks[current_task]['eta'], earliest_start[task_dependent_on_me])
                if tasks_to_complete[task_dependent_on_me] == 0:
                    current_tasks.append(task_dependent_on_me)
        if len(execution_order) == len(self.tasks):
            return [self.tasks[task_id]["name"] for task_id in execution_order], wave, earliest_start
        return None, None, None

    def get_execution_order(self) -> list:
        return self.get_execution_order_helper()[0]

    def get_available_tasks(self) -> list:
        """
        Get tasks that can be started right now.

        A task is available if:
            - Status is "todo"
            - All dependencies are "done"

        Returns:
            List of task names sorted alphabetically
        """
        available_tasks = []
        for task in self.tasks:
            all_ = True
            if self.tasks[task]["status"] != "todo":
                continue
            for dependency in self.tasks[task]["depends_on"]:
                if self.tasks[dependency]["status"] != "done":
                    all_ = False
                    break
            if all_:
                available_tasks.append(task)
        return sorted([self.tasks[task_id]["name"] for task_id in available_tasks])

    def get_parallel_groups(self) -> list:
        """
        Group tasks by execution "wave" (tasks in same group can run in parallel).

        Wave 0: Tasks with no dependencies
        Wave 1: Tasks whose dependencies are all in wave 0
        Wave N: Tasks whose dependencies are all in waves < N

        Returns:
            List of lists, each inner list contains task names (sorted) that can run together.
            Returns empty list if there's a cycle.
        """
        waves = self.get_execution_order_helper()[1]
        wave_inv = dict()
        for task_id in waves:
            if waves[task_id] not in wave_inv:
                wave_inv[waves[task_id]] = []
            wave_inv[waves[task_id]].append(self.tasks[task_id]["name"])
        waves = [sorted(wave_inv[wave])
                 for wave in list(sorted(wave_inv.keys()))]
        return waves

    # ==================== LEVEL 4: Critical Path ====================

    def set_duration(self, task_id: str, hours: float) -> bool:
        """
        Set the estimated duration for a task.

        Returns:
            True if set, False if task not found or hours <= 0
        """
        if task_id not in self.tasks:
            return False
        if hours <= 0:
            return False
        self.tasks[task_id]['eta'] = hours
        return True

    def get_earliest_start(self, task_id: str) -> float:
        """
        Get the earliest possible start time for a task.

        Earliest start = max(earliest_start + duration) of all dependencies
        Tasks with no dependencies start at time 0.

        Returns:
            Earliest start time as float.
            None if task not found or graph has cycle.
        """
        earliest_starts = self.get_execution_order_helper()[2]
        if task_id not in earliest_starts:
            return None
        print(earliest_starts)
        return earliest_starts[task_id]

    def get_project_duration(self) -> float:
        """
        Get the minimum time to complete all tasks (with unlimited parallelism).

        Returns:
            Total project duration.
            0.0 if no tasks or tasks have no duration set.
        """
        # TODO: Implement
        earliest_starts = self.get_execution_order_helper()[2]
        print(earliest_starts)
        max_time = 0
        for task_id in earliest_starts:
            max_time = max(
                max_time, earliest_starts[task_id] + self.tasks[task_id]['eta'])

        return max_time

    def get_critical_path(self) -> list:
        """
        Get the critical path - sequence of tasks where any delay delays the project.

        Returns:
            List of task names on the critical path, in execution order.
            Empty list if no tasks or graph has cycle.
        """
        _, waves, earliest_starts = self.get_execution_order_helper()
        wave_inv = dict()
        for task_id in waves:
            if waves[task_id] not in wave_inv:
                wave_inv[waves[task_id]] = []
            wave_inv[waves[task_id]].append(task_id)
        critical_path = []
        for wave in wave_inv:
            max_ = -1
            for task_id in wave_inv[wave]:
                if earliest_starts[task_id]+self.tasks[task_id]["eta"] > max_ and self.tasks[task_id]["eta"] != 0:
                    max_ = earliest_starts[task_id]+self.tasks[task_id]["eta"]
                    latest_task = task_id
            if max_ != -1:
                critical_path.append(self.tasks[latest_task]["name"])
        return critical_path
