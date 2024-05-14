import re

def extractParam(resp, sens, blacklist, placeholder):

    url_pattern = r'.*?:\/\/.*\?.*\=[^$]'
    found_urls = list(set(re.findall(url_pattern, resp)))
    modurls = []
    
    for url in found_urls:
        EqIndA = url.find('=')
        EqIndB = url.find('=', EqIndA +1)
        
        if blacklist:
            blacklist_regex = re.compile("|".join(blacklist))
            if not blacklist_regex.search(url):
                modurls.append(url[:EqIndA +1] + placeholder)
                if sens == 'high' and EqIndB != -1:
                    modurls.append(url[:EqIndB + 1] + placeholder)
        else:
            modurls.append(url[:EqIndA + 1] + placeholder)
            if sens == 'high' and EqIndB != -1:
                modurls.append(url[:EqIndB +1] + placeholder)
                
    return list(set(modurls))
