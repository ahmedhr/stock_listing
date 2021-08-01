import importlib


def get_stock_obj(stock_type: str):
    try:
        module = importlib.import_module(f"stock_app.stock_types.{stock_type}")
        stock_obj = getattr(module, f"{stock_type.title()}")
    except (ImportError, AttributeError):
        raise ValueError(f"Unknown format {stock_type!r}") from None

    return stock_obj
