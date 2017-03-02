gittext = run_command('git', 'log', '-n', '1', '--oneline').stdout().split()[0]

conf = configuration_data()
conf.set('GITVERSION', gittext)

configure_file(
    input : 'git_sha1.h.in',
    output : 'git_sha1.h',
    configuration : conf)

# May need to work around stuff here.
