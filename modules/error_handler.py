from fastapi.responses import JSONResponse


def value_error_exception_handler(error: ValueError):
    return JSONResponse(
        status_code=400,
        content=error
    )
