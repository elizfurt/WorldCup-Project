def user_dashboard(request):
    is_dashboard = request.resolver_match.url_name == 'userDashboard'
    print(f'is_dashboard: {is_dashboard}')
    return {'is_user_dashboard': is_dashboard}