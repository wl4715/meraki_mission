# New Catalyst & Meraki DevNet Test Drive
Meraki Mission for new Meraki &amp; Catalyst DevNet Test Drive

## Core track:
Provide audience the possibility to create a very simple network configuration template using APIs. 

1. ORG-WIDE -> Create network
2. ORG-WIDE -> Claim devices
3. MX -> Create VLANs
4. MS -> Assign to switch ports
5. MR -> Create SSIDs

## Bonus Mission:
**Option 1 - Flask or config file to use the tempalte more seamlessly**
- Dropdown list to share config with other non-API users

**Option 2 - Test Driven Automation**

Write a script to verify that the config correctly matches the desired one (linked to previous mission of Thousand Eyes)

For example, in wifi, many times users configure the wrong AP RF profile, and then they have wifi problems. Template we could use:
- https://github.com/obrigg/meraki-health-check
- https://github.com/obrigg/meraki-channel-distribution

**Option 3 - Catalyst Monitoring**

Use APIs for Catalyst monitoring in the Meraki Dashbaord (power of the platform)
