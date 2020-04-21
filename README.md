# Of Cash and Captcha

**Everything within this article is an opinion and should not be treated as fact. If you would like to research it: be my guest.**

In a move that can only be described as "cost-cutting", Cloudflare has abandoned Google's monolithic reCAPTCHA system in favor of the cheaper alternative: hCaptcha.

Under normal circumstances, I couldn't care less who Cloudflare partners with for their captcha system. These captchas take up mere seconds of my life; why should I care? Click a few boxes, proceed to the website, and life is goes on.

However, no longer do we have the trustworthy reCAPTCHA that's always been by our side. Now, we must suffer at the hands of the corporate overlords. We must now suffer with hCaptcha.

And suffer I did, with 8 select-the-image boxes. Anyone can handle clicking the old reCAPTCHA button; no problem. Further, selecting some images is no big deal. However, when hCaptcha forces a user to fill out 8 select-the-image captchas in a row, I'm sure there's a provision in the Geneva convention for that.

Mind you, this isn't any small subsection of websites that will be using hCaptcha through Cloudflare. This is essentially 10% of the modern internet [4] and I'd be cursed if I said nothing about it! So, let's begin.

## On the Matter of Privacy

Cloudflare would have you believe, according to their blog post [1], that this move was purely on a matter of privacy; that the users were what drove this decision. Obviously, this is exactly why the changes came only **AFTER** Google announced they would begin charging for extensive use of reCAPTCHA (I hope you're no stranger to sarcasm, reader). So, let's examine some of the practices conducted by hCaptcha and compare them to Cloudflare's aforementioned blog post.

To quote the first of many positives listed by Cloudflare:

> 1) they don't sell personal data; they collect only minimum necessary personal data, they are transparent in describing the info they collect and how they use and/or disclose it, and they agreed to only use such data to provide the hCaptcha service to Cloudflare

This is what most users should be concerned about. As I'm sure you would agree, having nana's cookies auctioned off to the CCP - or any other benevolent political party stationed in Europe/Asia - is disconcerting to say the slightest. Luckily, Cloudflare assures us that hCaptcha collects **only the minimum** to provide their service; they're also very transparent about it!

Ah, of course! This is exactly why hCaptcha sends the following metadata to their server [2]: screen height, screen width, window height, window width, color depth, browser build, browser vendor, browser agent, OS platform, CPU threads, user language, installed plugins, and mouse movements (while on the captcha page).

And, despite appearing empty in my testing, the following information could also be sent [2]: geolocation data, website permissions, and hardware devices.

Although this is enough information to fingerprint, identify, and track the user everywhere they go [5], hCaptcha has a wonderful policy of protecting that information! Let's take a look into their privacy policy [3]:

> We use the information we collect for the following purposes:
>
> ...
>
> For any legitimate business purpose, provided that the information is anonymized.

> We share or disclose information in the following cases:
>
> ...
>
> With others for any legitimate business purpose, provided the information is anonymized.

What exactly constitutes "anonymized" information? What constitutes a "legitimate business purpose"? Who are these "others" they may share it with? Well, your guess is as good as mine - and I'm sure neither of us are lawyers!

I think it's safe to say that a random blog post from Cloudflare, assuring us hCaptcha is privacy-oriented, trumps out the official hCaptcha privacy policy (don't get me started on how their accessibility features are locked behind email registration).

## On the Matter of Captcha

Not only does hCaptcha do a wonderful job of privacy through obscurity, their system also manages to catch bots like nothing (literally like nothing, in some cases)! For further details, watch with amazement as the supplied Python script **guesses answers and still passes hCaptcha without providing any of the supposed "minimum information."** Isn't technology wonderful?

![Passing hCaptcha is easy (for computers)!](images/passed.png)

## Closing Words

![Wise words](images/summary.png)

## Works Cited

1. Visited on 04/21/2020 https://blog.cloudflare.com/moving-from-recaptcha-to-hcaptcha/
2. Collected on 04/21/2020 Network analysis of hCaptcha's traffic.

3. Visited on 04/21/2020 https://www.hcaptcha.com/privacy
4. Visited on 04/21/2020 https://www.cloudflare.com/learning/what-is-cloudflare/

5. Visited on 04/21/2020 https://pixelprivacy.com/resources/browser-fingerprinting/