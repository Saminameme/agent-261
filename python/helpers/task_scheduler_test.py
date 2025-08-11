from python.helpers.task_scheduler import TaskPlan


def test_task_plan_create_returns_distinct_lists():
    plan_one = TaskPlan.create()
    plan_two = TaskPlan.create()
    assert plan_one.todo is not plan_two.todo
    assert plan_one.done is not plan_two.done

