#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:36:16 2018
CAMERA PTZ-MOVEMENTS
@author: kdg
"""
import zeep
from onvif import ONVIFCamera

def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue

zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue
    
def PTZmovez(camera=ONVIFCamera('172.17.4.190', 80, 'admin', 
    'admin'), arc='ContinuousMove', X=0, Y=0, Z=0):
    '''
    Camera movings - turn(panorama/tilt), zoom, home.
    May be absolute, relative & continuos
    '''
    media = camera.create_media_service()  # Create media service object
    ptz = camera.create_ptz_service()      # Create ptz service object
    profile = media.GetProfiles()[0]       # Get target MEDIA profile  
        # Get PTZ configuration options for getting move range of type
    request = ptz.create_type('GetConfigurationOptions')
    request.ConfigurationToken = profile.PTZConfiguration.token      
        
    request = ptz.create_type(arc)    # arc --> abs/rel/con  
    request.ProfileToken = profile.token  
    params = {'PanTilt': {}, 'Zoom': {}}
    
    if arc == 'AbsoluteMove':
        request.Position = params
        request.Position['PanTilt']['x'] = X
        request.Position['PanTilt']['y'] = Y
        request.Position['Zoom']['x'] = Z
        ptz.AbsoluteMove(request)
    elif arc == 'RelativeMove':
        request.Translation = params
        request.Translation['PanTilt']['x'] = X
        request.Translation['PanTilt']['y'] = Y
        request.Translation['Zoom']['x'] = Z
        ptz.RelativeMove(request)
    else:  # 'ContinuousMove'
        request.Velocity = params
        request.Velocity['PanTilt']['x'] = X
        request.Velocity['PanTilt']['y'] = Y
        request.Velocity['Zoom']['x'] = Z
        ptz.ContinuousMove(request)
        
if __name__ == '__main__':
    PTZmovez()            

        
        
        
            
            
            
           
        
