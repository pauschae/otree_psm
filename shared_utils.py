def app_number(player, app_name):
    return player.session.config['app_sequence'].index(app_name) + 1


def num_apps(player):
    return len(player.session.config['app_sequence'])


def common_template_vars(player, constants, app_name, **extra_vars):
    template_vars = dict(
        part_index=app_number(player, app_name),
    )

    if hasattr(constants, 'levels'):
        template_vars['levels'] = constants.levels

    if hasattr(constants, 'choices'):
        template_vars['choices'] = constants.choices

    template_vars.update(extra_vars)
    return template_vars
