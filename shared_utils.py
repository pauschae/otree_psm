def app_number(player, app_name):
    return player.session.config['app_sequence'].index(app_name) + 1

def num_apps(player):
    return len(player.session.config['app_sequence'])
    
def common_template_vars(player, constants, app_name):
    return dict(
        levels=constants.levels,
        choices=constants.choices,
        part_index=app_number(player, app_name),
    )