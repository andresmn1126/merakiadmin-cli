import meraki

dashboard = meraki.DashboardAPI(
    api_key='',
    print_console=False,
    output_log=False
)
template_id = 591097451092378819
org_list = dashboard.organizations.getOrganizations()


def getUserID(user_email):
    admin_list = dashboard.organizations.getOrganizationAdmins(template_id)
    try:
        admin_id = [admin['id'] for admin in admin_list if admin['email'] == user_email]
        return int(admin_id[0])
    except IndexError:
        print(f"{user_email} is not valid or does not exists, please check to ensure it was typed properly")
        return 0


def addAdmin():
    user_name = input('Please type the name of the person to be added\n')
    user_email = input('Please type the email of the person to be added\n')
    access_type = input('Type access type for the user, can be full or read-only\n')
    for org in org_list:
        try:
            dashboard.organizations.createOrganizationAdmin(org['id'], user_email, user_name, access_type)
            print(f"{user_name} successfully added to {org['name']}")
        except meraki.APIError as e:
            print(f'error = {e.message}')


def removeAdmin():
    user = input(f'Please enter the email for the user to be removed\n')
    user_id = getUserID(user)
    if user_id > 0:
        for org in org_list:
            try:
                dashboard.organizations.deleteOrganizationAdmin(org['id'], user_id)
                print(f"{user} successfully removed from {org['name']}")
            except meraki.APIError as e:
                print(f'error = {e.message}')






