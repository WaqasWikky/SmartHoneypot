import requests

def lookup_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data['status'] == 'success':
            return {
                "ip": ip,
                "country": data.get("country", ""),
                "region": data.get("regionName", ""),
                "city": data.get("city", ""),
                "isp": data.get("isp", ""),
                "org": data.get("org", ""),
                "lat": data.get("lat", ""),
                "lon": data.get("lon", "")
            }
        else:
            print(f"[x] IP lookup failed: {data.get('message', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"[x] Exception during IP lookup: {e}")
        return None
