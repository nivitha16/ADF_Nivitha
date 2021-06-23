from configparser import ConfigParser

file= "config.ini"
config=ConfigParser()
config.read(file)

print(config.sections())
print(list(config['INTERN']))

# config.add_section('INTERN')
# config.set('INTERN','Name','Nivi')
# config.set('INTERN','Age','20')
#
# print(config.sections())
# with open(file, 'w') as configfile:
#     config.write(configfile)