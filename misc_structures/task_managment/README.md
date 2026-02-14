# CodeSignal Interview Preparation - Task Dependency System

A practice project with progressive complexity requiring data structure evolution and algorithmic thinking.

## Overview

- **Time Target:** 90 minutes for all 4 levels
- **Language:** Python (standard library only)
- **Testing:** pytest
- **Focus:** Data structure design, graph algorithms, evolving requirements

## Running Tests

```bash
pytest test_task_system.py -v -k "level1"
pytest test_task_system.py -v -k "level2"
pytest test_task_system.py -v -k "level3"
pytest test_task_system.py -v -k "level4"
```

---

## Level 1: Basic Task Management (Estimated: 15 minutes)

Simple task creation and status management.

### Requirements

1. **Create tasks** with unique `task_id` and `name`
2. **Update status**: `todo` → `in_progress` → `done` (can only move forward)
3. **Get tasks by status** - return list of task names

### Methods to Implement

- `create_task(task_id: str, name: str) -> bool`
- `update_status(task_id: str, status: str) -> bool` (only forward transitions allowed)
- `get_tasks_by_status(status: str) -> list[str]` (names sorted alphabetically)
- `get_status(task_id: str) -> str | None`

### Key Challenge
- Design your task storage to be easily extensible for later levels

---

## Level 2: Dependencies (Estimated: 20 minutes)

Add dependencies between tasks. **This will require modifying your data structures.**

### New Requirements

1. **Add dependency** - task A depends on task B (B must be done before A can start)
2. **Validate status transitions** - can't move to `in_progress` unless all dependencies are `done`
3. **Detect circular dependencies** - adding a dependency that creates a cycle should fail
4. **Get blockers** - return which tasks are blocking a given task

### Methods to Implement

- `add_dependency(task_id: str, depends_on: str) -> bool` (fails if would create cycle)
- `get_blockers(task_id: str) -> list[str]` (names of incomplete dependencies, sorted)
- `update_status(...)` - now validates dependencies before allowing `in_progress`

### Key Challenge
- Cycle detection in a directed graph
- Your data structure needs to track both "depends on" and "depended by" efficiently

---

## Level 3: Execution Order (Estimated: 25 minutes)

Determine valid execution orders. **More graph algorithm work.**

### New Requirements

1. **Get execution order** - return ONE valid order to complete all tasks (topological sort)
2. **Get next available** - return tasks that can be started now (all deps done, status is `todo`)
3. **Parallel groups** - return tasks grouped by "wave" (tasks in same wave can run in parallel)

### Methods to Implement

- `get_execution_order() -> list[str] | None` (task names in valid order, None if impossible)
- `get_available_tasks() -> list[str]` (task names that can start now, sorted)
- `get_parallel_groups() -> list[list[str]]` (each inner list is tasks that can run together)

### Key Challenge
- Topological sort (Kahn's algorithm or DFS-based)
- Grouping by "depth" in the dependency graph

---

## Level 4: Critical Path (Estimated: 30 minutes)

Add time estimates and find the critical path. **Requires rethinking how you store/compute data.**

### New Requirements

1. **Set duration** - each task has an estimated duration (hours)
2. **Earliest start time** - when can a task start at the earliest?
3. **Total project time** - minimum time to complete all tasks (with unlimited parallelism)
4. **Critical path** - tasks where any delay delays the whole project

### Methods to Implement

- `set_duration(task_id: str, hours: float) -> bool`
- `get_earliest_start(task_id: str) -> float | None` (None if has incomplete cycle)
- `get_project_duration() -> float` (total time with unlimited parallelism)
- `get_critical_path() -> list[str]` (task names on critical path, in order)

### Key Challenge
- Forward pass to compute earliest start times
- Backward pass to compute latest start times  
- Critical path = tasks where earliest == latest start time

---

## Data Structure Evolution Tips

**Level 1:** Simple dict might work
```python
self.tasks = {task_id: {"name": ..., "status": ...}}
```

**Level 2:** Need to add graph edges
```python
self.tasks[task_id]["depends_on"] = set()
self.tasks[task_id]["dependents"] = set()  # reverse edges for efficiency
```

**Level 3:** May need to cache topological order or depth

**Level 4:** Need to store durations and possibly cache computed times
```python
self.tasks[task_id]["duration"] = ...
self.tasks[task_id]["earliest_start"] = ...  # cached or computed on demand?
```

---

## Algorithm Hints (only read if stuck)

<details>
<summary>Cycle Detection</summary>
Use DFS with three colors: white (unvisited), gray (in current path), black (done).
If you visit a gray node, there's a cycle.
</details>

<details>
<summary>Topological Sort</summary>
Kahn's algorithm: Start with nodes that have no dependencies, remove them, repeat.
Or: DFS post-order gives reverse topological order.
</details>

<details>
<summary>Critical Path</summary>
1. Forward pass: earliest_start[t] = max(earliest_start[dep] + duration[dep]) for all deps
2. Backward pass: latest_start[t] = min(latest_start[dependent] - duration[t])
3. Critical: earliest_start[t] == latest_start[t]
</details>

Good luck! 🚀
