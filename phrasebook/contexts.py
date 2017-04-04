def get_sidebar_args(request):
    ctx = {'name': request.user.first_name + " " + request.user.last_name[0:1] + "."}
    return ctx