import time
import logging
from django.core.cache import cache
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class RequestTimingMiddleware:

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		start_time = time.time()

		# actuall calling of view
		response = self.get_response(request)

		end_time = time.time()
		duration = end_time - start_time
		logger.info(
				f"Path: {request.path}"
				f"Method: {request.method}"
				f"Duration: {duration}"
			)
		print(f"Path: {request.path}"
				f"Method: {request.method}"
				f"Duration: {duration}")
		response["X-Response-Time"] = f"{duration:.4f}s"

		return response


class RateLimitMiddleware:

	RATE_LIMIT = 5
	TIME_WINDOW = 60

	def __init__(self, get_response):
		self.get_response = get_response

	def get_client_ip(self, request):
		ip_addr = request.META.get("HTTP_X_FORWARDED_FOR")
		if ip_addr:
			return ip_addr
		return request.META.get("REMOTE_ADDR")

	def __call__(self, request):
		ip = self.get_client_ip(request)

		cache_key = f"rate_limit_{ip}"
		request_count = cache.get(cache_key, 0)

		if request_count >= self.RATE_LIMIT:
			return JsonResponse({"error": "Too Many Requests"}, status=429)

		cache.set(
			cache_key,
			request_count+1,
			timeout = self.TIME_WINDOW
		)


		response = self.get_response(request)
		return response

