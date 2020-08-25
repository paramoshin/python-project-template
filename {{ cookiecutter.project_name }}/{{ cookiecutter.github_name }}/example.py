"""Example module."""
__all__ = ["hello"]


def hello(name: str) -> str:
    """This function greets you.

    Example function.

    Args:
        name (str): Name to greet.

    Returns:
        A greeting message.

    Example:
        >>> hello("World")
        "Hello, World!"
    """
    return f"Hello, {name}!"
