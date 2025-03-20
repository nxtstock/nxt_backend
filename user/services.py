from modules.error_handler import value_error_exception_handler


def create_user_data_service(request):
    try:
        if request.account_type == "NSDL":
            pass
        elif request.account_type == "CDSL":
            pass
        else:
            return {
                f"Choose Wrong Account Type {request.account_type}"
            }

    except Exception as e:
        return value_error_exception_handler(e)
