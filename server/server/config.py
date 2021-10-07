from fastapi.responses import ORJSONResponse

# Sets district code for accessing renweb. If self-deploying you may have to change this.
districtCode = "BC-THA"
districtCodeUrl = districtCode.lower()

# Response type. See fastapi docs https://fastapi.tiangolo.com/advanced/custom-response/ for availble values.
JSONresponse = ORJSONResponse
