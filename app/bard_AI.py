from bardapi import BardCookies

def bard_AI(prompt):
    cookie_dict = {
        "__Secure-1PSID": "eQjkGyjE_FtCX8RzYi-VYHr7R1JmHC17DDh2289vbX8DlgFu6vbdSrzN1XyyzH_MrIOz_A.",
        "__Secure-1PSIDTS": "sidts-CjIBPVxjSq3FrTS0uYVvbiRZcPsOAmOjymXRXoVPfFcrxCgVqBQLWxDhlhSoCa4VAYUGMhAA",
        "__Secure-1PSIDCC": "ABTWhQGISO4rNODv2TtoKtLM4r4Tu-jtA04kxm_UGiayUbZDtSu348CpDHPUehxY4gF2fGMSf7Y",
        # Any cookie values you want to pass session object.
    }

    bard = BardCookies(cookie_dict=cookie_dict)
    return (bard.get_answer(prompt)['content'])