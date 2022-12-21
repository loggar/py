list1 = ('CN=Garen Demacia,OU=ENROL,DC=OUR_CLIENT,DC=LOCAL', {'primaryGroupID': ['513'], 'logonCount': ['173'], 'cn': ['Garen Demacia'], 'countryCode': ['0'], 'dSCorePropagationData': ['20190423154607.0Z', '16010101000000.0Z'], 'objectClass': ['top', 'person', 'organizationalPerson', 'user'], 'userPrincipalName': ['garen@OUR_CLIENT.LOCAL'], 'lastLogonTimestamp': ['132054597221134835'], 'instanceType': ['4'], 'distinguishedName': ['CN=Garen Demacia,OU=ENROL,DC=OUR_CLIENT,DC=LOCAL'], 'sAMAccountType': ['805306368'], 'objectSid': ['\x01\x05\x00\x00\x00\x00\x00\x05\x15\x00\x00\x00CSr\x07\xa0U\x94K\xa5a\x10\x87\xf5U\x00\x00'], 'whenCreated': [
         '20181221043621.0Z'], 'uSNCreated': ['4093135'], 'badPasswordTime': ['131981149128090429'], 'pwdLastSet': ['131898405818944349'], 'sAMAccountName': ['garen'], 'objectCategory': ['CN=Person,CN=Schema,CN=Configuration,DC=OUR_CLIENT,DC=LOCAL'], 'objectGUID': ['R{\x98g\xef1NM\xb8\x12~b\xc8\x05Q&'], 'whenChanged': ['20190619232016.0Z'], 'badPwdCount': ['0'], 'accountExpires': ['9223372036854775807'], 'displayName': ['Garen Demacia'], 'name': ['Garen Demacia'], 'codePage': ['0'], 'userAccountControl': ['66048'], 'lastLogon': ['132054600373135284'], 'uSNChanged': ['4728375'], 'sn': ['Demacia'], 'givenName': ['Garen'], 'lastLogoff': ['0']})

list2 = ('OU=Library Computers,OU=ENROL,DC=OUR_CLIENT,DC=LOCAL', {'distinguishedName': ['OU=Library Computers,OU=ENROL,DC=OUR_CLIENT,DC=LOCAL'], 'dSCorePropagationData': ['20190423154652.0Z', '20190423154645.0Z', '20190423154607.0Z', '20190423154607.0Z', '16010101000000.0Z'], 'name': ['Library Computers'], 'objectCategory': ['CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=OUR_CLIENT,DC=LOCAL'], 'objectClass': [
         'top', 'organizationalUnit'], 'gPLink': ['[LDAP://cn={94EF6BC2-35F2-432D-A340-B3100F660142},cn=policies,cn=system,DC=OUR_CLIENT,DC=LOCAL;2]'], 'objectGUID': ['\x9bqwYz\x0c\xb6H\x87\xd4\xe3\xdd\x9dL\xf9\xd3'], 'whenChanged': ['20190423161923.0Z'], 'whenCreated': ['20190423154607.0Z'], 'uSNCreated': ['4508327'], 'uSNChanged': ['4508484'], 'ou': ['Library Computers'], 'instanceType': ['4']})

print(list1)

if 'cn' in list1[1]:
    print(list1[1]['cn'])

if 'cn' not in list2[1]:
    print('list2[1] has no key', 'cn')
