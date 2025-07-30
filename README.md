# 🕷️ streamlit-snooping

> helps interacting with streamlit webapp behind domain name

requirements
```
/_stcore/host-config has allowedOrigins and no useExternalAuthToken
```

drop cors before browsing to your streamlit url in this webapp
```
# tested in kali linux
chromium --disable-web-security --use-data-dir=/tmp/chromium-nocors
```
