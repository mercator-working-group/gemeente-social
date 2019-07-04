TOC?

# gemeente-social
An analysis of social media presence on official municipal websites of the Netherlands

## Overview
`gemeente-social` is a repository for investigative and analystical work specific to the prevalence of social media resources appearing on official websites belonging to municipalities in the Netherlands. This repository contains parameters used in this investigation and analyses perfomred to provide aggregate and annecdotal reporting on the useage of third-party commuinication and social platforms by govenmental municipal parties.

## Dependencies
The instrumentation of the crawl used to collect data fro municipal websites for the gemeente-social project accomplished using a [custom fork](https://github.com/mercator-working-group/OpenWPM) of the [OpenWPM](https://github.com/mozilla/OpenWPM) web privacy measurement framework, developed by Steven Engelhardt at [Princeton univesity](https://webtap.princeton.edu/), currently hosted and maintained by [Mozilla](mozilla.org). 

## Workflow: region agnostic examination of private communication infrastructure by governmental entities

  - Accept an arbitrary seed list of government websites
  - Determine one-depth a-tag linkage structure with a shallow preliminary crawl
  - Perform a comprehensive crawl using OpenWPM to instrument JavaScript events at page visit
  - Parse OpenWPM data into Pandas table
  - Match agaunst an arbitrary 
  - Indentify specific tracking pixels and potential fingerprinting attacks focussing on third-party loaded resources.
  - Generate a report of third-party resources and tracking activity occuring per page (from originally provided seed-list).

## Analyses
TBC 

# FAQ

### When was the data used in this analysis collected?
The most recent full pre-crawl and comprehensive (OpenWPM) crawls were executed on May 29th, 2019 (UTC+2)


