#!/usr/bin/env python3
from requests import Session
from secrets import choice
from time import time
from uuid import uuid4


class CaptchaEngine(Session):
	def __init__(self):
		super().__init__()
		self.headers.update({
			'User-Agent': choice((
				'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko)',
				'Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36',
				'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
			))
		})

	def bypass_captcha(self, host):
		# Now would be a good time to mention some of the advanced features:
		# 1. The  system is so developer-friendly that any UUID4 will pass as the correct site key.
		# No more worrying about typos or bad coding, the backend allows all keys to pass!
		site_key = str(uuid4())

		response = self.post('https://hcaptcha.com/getcaptcha', data={
			'sitekey': site_key,
			'host': host
		}).json()

		# Technical details to get out of the way.
		key = response.get('key')
		tasks = [row['task_key'] for row in response.get('tasklist')]
		job = response.get('request_type')
		timestamp = round(time()) + choice(range(30, 120))

		# 2. State-of-the-art cryptographic randomness passes for "human" answers.
		# Although many have flagged this as a BUG, it is most definitely a FEATURE.
		# You see, "human" input should be indistinguishable from randomness; everyone knows that!
		answers = dict(zip(tasks, [choice(['true', 'false']) for index in range(len(tasks))]))

		# 3. The backend has been fully optimized to ignore some information passed!
		# Many questions I'm sure we will receive are: "If you don't use the data
		# for human-verification purposes, why send it at all?"
		# What a great question! You see, the answer lies in this unique policy.
		# If it's there, might as well collect it - even if it's unnecessary!
		# This reduces the codebase for captcha checking AND keeps the 700GB
		# SQLite database growing!
		mouse_movements = []
		last_movement = timestamp

		for index in range(choice(range(1000, 10000))):
			last_movement += choice(range(10))
			mouse_movements.append([choice(range(500)), choice(range(500)), last_movement])

		response = self.post(f'https://hcaptcha.com/checkcaptcha/{key}', json={
			'answers': answers,
			'sitekey': site_key,
			'serverdomain': host,
			'job_mode': job,
			'motionData': {
				'st': timestamp,
				'dct': timestamp,
				'mm': mouse_movements
			}
		}).json()

		return response.get('pass') == True


def main():
	engine = CaptchaEngine()
	bypassed = engine.bypass_captcha('www.escapefromtarkov.com')

	if bypassed:
		print('[+] The hCaptcha was bypassed completely.')
	else:
		# Don't let this error get you down, just re-run it a few times!
		# The backend is very lenient, so just ask nicely to pass.
		print('[-] For some reason, hCaptcha failed our attempt!')


if __name__ == '__main__':
	main()
