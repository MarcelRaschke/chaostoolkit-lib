from typing import Any, Dict, List

from chaoslib.types import (
    Activity,
    Configuration,
    Experiment,
    Hypothesis,
    Journal,
    Run,
    Secrets,
    Settings,
)


def configure_control(
    experiment: Experiment,
    configuration: Configuration,
    secrets: Secrets,
    settings: Settings,
) -> None:
    experiment["configure_control_secrets"] = secrets


def cleanup_control() -> None:
    pass


def before_experiment_control(context: Experiment, secrets: Secrets, **kwargs) -> None:
    context["before_experiment_control_secrets"] = secrets


def after_experiment_control(
    context: Experiment, state: Journal, secrets: Secrets, **kwargs
) -> None:
    context["after_experiment_control_secrets"] = secrets


def before_hypothesis_control(
    context: Hypothesis, experiment: Experiment, secrets: Secrets, **kwargs
) -> None:
    experiment["before_hypothesis_control_secrets"] = secrets


def after_hypothesis_control(
    context: Hypothesis,
    experiment: Experiment,
    state: Dict[str, Any],
    secrets: Secrets,
    **kwargs
) -> None:
    experiment["after_hypothesis_control_secrets"] = secrets


def before_method_control(context: Experiment, secrets: Secrets, **kwargs) -> None:
    context["before_method_control_secrets"] = secrets


def after_method_control(
    context: Experiment, state: List[Run], secrets: Secrets, **kwargs
) -> None:
    context["after_method_control_secrets"] = secrets


def before_rollback_control(context: Experiment, secrets: Secrets, **kwargs) -> None:
    context["before_rollback_control_secrets"] = secrets


def after_rollback_control(
    context: Experiment, state: List[Run], secrets: Secrets, **kwargs
) -> None:
    context["after_rollback_control_secrets"] = secrets


def before_activity_control(
    context: Activity, experiment: Experiment, secrets: Secrets, **kwargs
) -> None:
    experiment["before_activity_control_secrets"] = secrets


def after_activity_control(
    context: Activity, experiment: Experiment, state: Run, secrets: Secrets, **kwargs
) -> None:
    experiment["after_activity_control_secrets"] = secrets
