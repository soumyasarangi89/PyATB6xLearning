api_response = int(input("Enter Response Code : "))

retry = 1
success = False

if api_response == 200:
    print(f"Response: {api_response} Ok \n✅ Test Passed")
    success = True
else:
    while retry < 3 and not success:
        print("Session Timeout, Retry")
        retry += 1
        api_response = int(input(f"Retry {retry}, Enter Response Code : "))

        if api_response == 200:
            print(f"Response: {api_response} Ok \n✅ Test Passed")
            success = True
if not success:
    print(f"All {retry} attempts failed,\n❌ Test Failed")