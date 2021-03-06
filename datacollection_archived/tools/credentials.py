import tweepy

#Credentials
cred_dict={'Thesis':{'ckey':[],'csecret':[],'atoken':[],'asecret':[]}} #Create Dictionary for each account
cred_dict['Thesis']['ckey']=["oGymKwaEmMih2Evpvpf6OdM5L", "TAYFiq08g0dJRaOKJ1pjGypVA", "ntXOwYjbkWvM5kWwRGsWYlvle", "BunkTdfFjElcShsRSdTbZaIKk", "y5grj20yonP4EA53PAcw6rGbg", "5WVQongz712qT0InemuhgE1J0", "cr15DGQqza5hP9nY35SSxJkqm"] #I use lists as I have multiple apps per account
cred_dict['Thesis']['csecret']=["azWdvSiYYi1ciIYqXh8D8Z1IzAUFGrR4pMr7srLNiZe7leUe9V", "mTL3hxg9KkXdAUwczb4hCEj9LTRvez20ywxzlAV1cxddAETXXe", "52f3l6Sx4j2zrs7xcjb4PNOuxnGCnjkUCG6XHQf2FuJ4T6G2ne", "J4RENeHecKS4PRKs7tP0KsjxW8mhT1xpHmBnMh2TZgsOPBReWj", "wwOhDD4pzhWXEjEtMtOoss5PtDbpnf26PWXoKZy44aEtoikjtZ", "KXmwIpFY2dS3LkEmnBwI4sdxSMkAh8CxHecHR5i5bFQvpocKBs", "NLLhTpNMke331OuFdf2OUsXGWmScW0xQVFpDa37xthzxgZxOrz"]
cred_dict['Thesis']['atoken']=["1051549838792364035-t2PvjyeXW3UIsQuH7l00MxdhXxYReD", "1051549838792364035-TuVg6QFOYhBlGKYfHM7sj60guO1xCc", "1051549838792364035-ThZ0KsVBTVFWVebOumlY7ZLG0iEJTT", "1051549838792364035-FKFsITF3yPQoXlwZTx5nMpI9eod4N5", "1051549838792364035-QVyABqOILqs76p0OWorqu7xAhMWzPY", "1051549838792364035-B2DfeZeJLRXiYFKLScJw4NJDhbFV6o", "1051549838792364035-rPf7gu2mtBfVIqplNPvblggu78dIDO"]
cred_dict['Thesis']['asecret']=["ob7MhEOhFykrggxvPpxc8qnjE0aO9xSrVY9UgIhFRG1m1pr", "k9ua4w2PH3d6BSYvLfaFjaJCmVg5mZ0tjT0wXGezQwlzH", "HXGsnXHvGZcztssvz4qmV76MVk171K6AOfP8EYVCXNsyQ", "XrjbjcFOtU2gUX8nIk7nCyzUrfrapSrMkOybcYFYzZI7z", "lsJaxJK7xy5jgqYsPsdycDps2R0wJEWfoZvImPoBsJp12", "GR2duCp7A5QeT05dLuz7iMIfXUgzBvyRcrRuMKwJP51O0", "SAFLZPfguWah4doQGgPCoLYVJyVviOaOgk9Z08BNFtSbZ"]

### App-User Authorization

"""

https://developer.twitter.com/en/docs/basics/rate-limits

"""

def getAuth(i, mode):
    ckey = cred_dict['Thesis']['ckey'][i]
    csecret = cred_dict['Thesis']['csecret'][i]
    atoken = cred_dict['Thesis']['atoken'][i]
    asecret = cred_dict['Thesis']['asecret'][i]
    auth = authorizer(ckey,csecret,atoken,asecret, mode)
    return auth


def authorizer(ckey,csecret,atoken=None,asecret=None, mode="user"):
    """
    Ramon:
    :mode: either "user" or "app". "user" requires access tokens also.
    :return: corresponding API authorization
    """
    if mode == "user":
        auth = tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret) 
    else:
        auth = tweepy.AppAuthHandler(ckey, csecret)
        
    return auth
