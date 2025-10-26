import requests

BASE = "http://FastAp-ApiLB-xEq5mhe2Zpi7-908650413.us-east-1.elb.amazonaws.com"  # <-- your real value

print(requests.get(f"{BASE}/", timeout=10).json())
print(requests.post(f"{BASE}/predict-sentiment",
                    json={"text": "I love this service!"},
                    timeout=120).json())


'''
FastApiFargateStack.ApiLoadBalancerDNSB0038DD0 = FastAp-ApiLB-xEq5mhe2Zpi7-908650413.us-east-1.elb.amazonaws.com
FastApiFargateStack.ApiServiceURL135D4FCA = http://FastAp-ApiLB-xEq5mhe2Zpi7-908650413.us-east-1.elb.amazonaws.com
FastApiFargateStack.ServiceURL = http://FastAp-ApiLB-xEq5mhe2Zpi7-908650413.us-east-1.elb.amazonaws.com

'''