s1 = '''
Workaround:

The issue is fixed in 8.1(1) and higher release as well as the 7.3(1)D1(1B), 7.3(2)D1(1) and higher releases.

exclude
'''

s2 = '''
[taoji_ALI_N7K_6.2(16)_Jan_PCBA_2019]

Exclude.As per Eng-notes: Created 01/17/2017 14:10:02 Added 01/17/2017 14:10:02 by shreenik

- Affects Only Nexus 7700 M3-Series 40 Gigabit Cards.

No M3-cards as per HW list.
'''

s3 = '''
[xiaogyan_ICBC_N7K_6.2(16)_PCBA_Jan-2019-S1] 

Exclude. 

As per Eng-notes: 

- Affects Only Nexus 7700 M3-Series 40 Gigabit Cards.



No M3-cards as per requirements."
'''

s4 = '''
[null_excl,+RNE,+2 SR]Exclude.

As per DE: - Affects Only Nexus 7700 M3-Series 40 Gigabit Cards

https://search-prd.cisco.com/topic/news/cisco/cs/ca-defect-feedback/dsc830240.html
'''

s5 = '''
Exclude.

As per DE: - Affects Only Nexus 7700 M3-Series 40 Gigabit Cards

https://search-prd.cisco.com/topic/news/cisco/cs/ca-defect-feedback/dsc830240.html



Not our HW. Also as per VR: 8.1(0.86), TR should be safe.
'''

s6 = '''
[null_excl,+1 SR]Exclude:

As per DE: Yes Both fix are available in 8.1.1.

https://search-prd.cisco.com/topic/news/cisco/cs/ca-defect-feedback/dsc966978.html
'''

s7 = '''
Hence, our TR must be safe. Exclude.

As per DE: - Affects Only Nexus 7700 M3-Series 40 Gigabit Cards

https://search-prd.cisco.com/topic/news/cisco/cs/ca-defect-feedback/dsc830240.html
'''

s8 = '''
Exclude.

As per DE: - Affects Only Nexus 7700 M3-Series 40 Gigabit Cards

https://search-prd.cisco.com/topic/news/cisco/cs/ca-defect-feedback/dsc830240.html



Not our HW. Also as per VR: 8.1(0.86), TR should be safe.
'''

s9 = '''
Exclude:

As per DE: Yes Both fix are available in 8.1.1.

https://search-prd.cisco.com/topic/news/cisco/cs/ca-defect-feedback/dsc966978.html



Hence, our TR must be safe.
'''

s10 = '''
Exclude.

As per DE: - Affects Only Nexus 7700 M3-Series 40 Gigabit Cards

https://search-prd.cisco.com/topic/news/cisco/cs/ca-defect-feedback/dsc830240.html



Not our HW. Also as per VR: 8.1(0.86), TR should be safe.
'''

s11 = '''
[jamexu_ CCBA_ N7K _6.2(16) _PSRR_July-2018]

Per DE: Q: Will this be impacting 6.2(12) release on N7K?

               A: M3 is not supported on 6.2, so will not.

https://search-prd.cisco.com/topic/news/cisco/cs/ca-defect-feedback/dsc1032313.html

TR is safe. Exclude.
'''

s12 = '''
Exclude.

DE: - Affects Only Nexus 7700 M3-Series 40 Gigabit Cards

https://search-prd.cisco.com/topic/news/cisco/cs/ca-defect-feedback/dsc830240.html


Affects Only Nexus 7700 M3-Series 40 Gigabit Cards

https://search-prd.cisco.com/topic/news/cisco/cs/ca-defect-feedback/dsc830240.html
'''

s13 = '''
Per Eng-notes: Created 01/17/2017 14:10:02 Added 01/17/2017 14:10:02 by shreenik

- Affects Only Nexus 7700 M3-Series 40 Gigabit Cards

No M3 line-cards

Exclude

'''

s14 = '''
Note: This issue affects only Nexus 7700 M3-Series 40 Gigabit Cards. 



This issue has a functional impact.



Description:

M3 CB40 module went down itself and failed to come back. One had to manually power on the module.



Trigger:

Issue is seen during normal operation. No specific trigger for this issue. The probability of hitting this issue is frequent.



Workaround:

There is no workaround apart from Software Upgrade with the fix



This is an externally found issue with 1 service request. This issue is fixed in 8.0(1)E1.'''

information = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]