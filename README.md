# chinalist
[![GitHub last commit](https://img.shields.io/github/last-commit/Rongronggg9/chinalist?label=updated)](https://github.com/Rongronggg9/chinalist/commits)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Rongronggg9/chinalist/update-chinalist.yml)](https://github.com/Rongronggg9/chinalist/actions/workflows/update-chinalist.yml)

## Usage
### [SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega)
1. Open SwitchyOmega settings
1. Go to an auto-switching profile configuration page (create one if needed)
    1. Set `Rule List Format` to `AutoProxy`
    1. Fill in `Rule List URL` with the URL of [chinalist_omega.txt](https://raw.githubusercontent.com/Rongronggg9/chinalist/main/chinalist_omega.txt) 
    (or you may use [jsDelivr CDN](https://cdn.jsdelivr.net/gh/Rongronggg9/chinalist@latest/chinalist_omega.txt))
    1. Set `Rule list rules` to `DIRECT`, `Default` to a proxy server profile
    1. Click on `Download Profile Now` and then click on `Apply changes`
1. Switch to this auto-switching profile

### [SmartProxy](https://github.com/salarcode/SmartProxy)
1. Open SmartProxy settings
1. Go to `Proxy Rules Subscriptions`
    1. Click on `Subscribe to a rules list`
        1. Fill in `Url` with the URL of [chinalist_smart.txt](https://raw.githubusercontent.com/Rongronggg9/chinalist/main/chinalist_smart.txt) 
        (or you may use [jsDelivr CDN](https://cdn.jsdelivr.net/gh/Rongronggg9/chinalist@latest/chinalist_smart.txt))
        1. Set `Obfuscation` to `None`
        1. Set `Format` to `AutoProxy/GFWList`
        1. Leave `Username` and `Password` blank
        1. Save
    1. Save
1. Go to `Proxy Rules`
    1. Click on `Add Rule`
        1. Set `Rule Type` to `Host regex`
        1. Leave `Rule Source Domain` blank
        1. Fill `Url Regex` with `.*`
        1. Set `Proxy Server` to `[General]`, `Action` to `Apply proxy`
        1. Save
    1. Save
1. Switch to Smart Proxy mode


## Thanks
[pexcn/daily](https://github.com/pexcn/daily)