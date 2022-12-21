@echo off
%ERRORLEVEL%==0

cmdow /ma

## right_main
cmdow "*Sidebery*" /Res
cmdow "*Sidebery*" /mov 0 0
cmdow "*Sidebery*" /siz 2194 1186
        

## left_half_left
cmdow "*Google Chat*" /Res
cmdow "*Google Chat*" /mov -2566 0
cmdow "*Google Chat*" /siz 1283 1392
        

## left_half_right
cmdow "*Webex*" /Res
cmdow "*Webex*" /mov -1283 0
cmdow "*Webex*" /siz 1283 1392
        
cmdow "*Google Chat*" /act