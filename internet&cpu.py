import webbrowser
import time

def open_links_with_delay(links, delay_seconds=10):
    for link in links:
        webbrowser.open(link)
        time.sleep(delay_seconds * 10 )  # Convert minutes to seconds

if __name__ == "__main__":
    # PEUGEOT & CADILLAC :
    user_links = [
        "https://www.bing.com/search?FORM=KCEXPL&q=Internet&filters=sid:%225ddbc511-131a-4f60-9916-58f1b8db9a3c%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22",
        "https://www.bing.com/search?FORM=KCEXPC&q=network+topology&filters=sid:%22728d5810-a491-ffe9-35e4-88f01e6eaaf1%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=local+area+network&filters=sid:%22197be3b7-28d0-f8a3-23bd-995877005ffa%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=computer+hardware&filters=sid:%2222a95f44-1398-9bf1-ab66-103e5807f16c%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=computer+hardware&filters=sid:%2222a95f44-1398-9bf1-ab66-103e5807f16c%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Router&filters=sid:%22a5166787-954c-5dc7-0106-718d6eb4f062%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Ethernet&filters=sid:%226ce07d6f-a2f4-4023-08d4-738143608420%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Server&filters=sid:%221facb250-074e-5b19-fd5a-c91940bc59f4%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=communications+satellite&filters=sid:%2234ac5d0f-e076-d0cd-504e-11f7302fc2b6%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Telecommunications&filters=sid:%22ecb65d99-0258-0482-dfe4-b97c7ff37b5f%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=osi+model&filters=sid:%221b296525-cd07-a84c-6c57-e7c3a2a176b2%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Computer&filters=sid:%2245ab54f1-1ed9-8c38-7736-bf0ed054730a%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=denial-of-service+attack&filters=sid:%2267e12d82-bddc-9aea-cc7a-148a04d0c8a8%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Software&filters=sid:%221c919d01-ffcc-1f0a-fa8b-82c6a6cd9f79%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=1536&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=network+interface+controller&filters=sid:%22855ab1fc-4523-3fab-e223-4b82d5d603d6%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=1536&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Peer-to-peer&filters=sid:%2244cfdf3b-7ee6-84d9-ba63-8a2fddc46226%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=1536&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Email&filters=sid:%224b2d5ad5-72cb-b4d9-8655-6a55a712272a%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=1536&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=ieee+802.11&filters=sid:%225a9f7ce6-3545-83dc-21f4-5df4a9a9056e%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=1536&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=wide+area+network&filters=sid:%220d381257-d508-915b-eb13-69a4b7fab7a1%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=1536&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=twisted+pair&filters=sid:%2270a810eb-1407-270e-721a-40d2b606301c%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=1788&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=operating+system&filters=sid:%2268605fee-4e51-25c8-548b-65ea58400639%22+lite:%22.S2NkUmVsYXRpb25eMTg0NGZkOWMtMzk3My1kMzY5LTAzOWYtZDZiYzgwNTQyYjZjXl5eXiRFbnRpdHkyX2Vu%22&crslsl=1788&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPL&q=central+processing+unit&filters=sid:%228926169f-ff7b-b2dc-2e09-eccd896779a3%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22",
        "https://www.bing.com/search?FORM=KCEXPC&q=read-only+memory&filters=sid:%22c96aaaa0-d1dc-6b37-e2c5-f6ee9c552785%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=hard+disk+drive&filters=sid:%228b953795-6b56-06f1-dee7-4f3ceb676d46%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=data+storage&filters=sid:%22feb181fd-8860-6d66-42b7-6ce1c3fd9577%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=computer+hardware&filters=sid:%2222a95f44-1398-9bf1-ab66-103e5807f16c%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=random-access+memory&filters=sid:%229403514a-d8fa-8648-cbcb-475e67f27652%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=0&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=computer+memory&filters=sid:%22fc26872d-5fb2-08e8-9b78-6d61666da336%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=stockage+d%27information&filters=sid:%2238af65ae-441f-fb81-a465-83b521c500da%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Computer&filters=sid:%2245ab54f1-1ed9-8c38-7736-bf0ed054730a%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Motherboard&filters=sid:%223ee07698-b617-6505-ab2d-9032bf369879%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=dynamic+random-access+memory&filters=sid:%221ba37236-efad-8c56-fb84-a9f79a7534e7%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=Cache&filters=sid:%22ce6f53b0-49c7-180b-57c7-a3410da3a5ec%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=768&efirst=1",
        "https://www.bing.com/search?FORM=KCEXPC&q=solid-state+drive&filters=sid:%225d7ef07c-be3a-a7bc-ae19-9be46cdb74e0%22+lite:%22.S2NkUmVsYXRpb25eYjRmMGMzZDgtOTYyNS01YzQyLTA2OWYtYmMzNWNhZjFiOTZlXl5eXiRFbnRpdHkyX2Vu%22&crslsl=1536&efirst=1",

     ]
    
    
    user_delay_seconds = 1  # Adjust the delay as needed

    open_links_with_delay(user_links, user_delay_seconds)
