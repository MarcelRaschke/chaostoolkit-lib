from typing import Any, Dict, List

from chaoslib.types import (
    Activity,
    Configuration,
    Experiment,
    Hypothesis,
    Journal,
    Run,
    Secrets,
)

value_from_config = None


def configure_control(configuration: Configuration, secrets: Secrets) -> None:
    global value_from_config
    value_from_config = configuration.get("dummy-key", "default")


def cleanup_control() -> None:
    global value_from_config
    value_from_config = None


def before_experiment_control(context: Experiment, **kwargs) -> None:
    context["before_experiment_control"] = True


def after_experiment_control(context: Experiment, state: Journal, **kwargs) -> None:
    context["after_experiment_control"] = True
    state["after_experiment_control"] = True


def before_hypothesis_control(
    experiment: Experiment, context: Hypothesis, **kwargs
) -> None:
    context["before_hypothesis_control"] = True
    context["has_experiment_before"] = experiment is not None


def after_hypothesis_control(
    experiment: Experiment, context: Hypothesis, state: Dict[str, Any], **kwargs
) -> None:
    context["after_hypothesis_control"] = True
    state["after_hypothesis_control"] = True
    context["has_experiment_after"] = experiment is not None


def before_method_control(context: Experiment, **kwargs) -> None:
    context["before_method_control"] = True


def after_method_control(context: Experiment, state: List[Run], **kwargs) -> None:
    context["after_method_control"] = True
    state.append("after_method_control")


def before_rollback_control(context: Experiment, **kwargs) -> None:
    context["before_rollback_control"] = True


def after_rollback_control(context: Experiment, state: List[Run], **kwargs) -> None:
    context["after_rollback_control"] = True
    state.append("after_rollback_control")


def before_activity_control(
    experiment: Experiment, context: Activity, **kwargs
) -> None:
    context["before_activity_control"] = True
    context["has_experiment_before"] = experiment is not None


def after_activity_control(
    experiment: Experiment, context: Activity, state: Run, **kwargs
) -> None:
    context["after_activity_control"] = True
    state["after_activity_control"] = True
    context["has_experiment_after"] = experiment is not None
