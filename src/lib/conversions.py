import math


def peak2rms(peak_value):
    """peak2rms Convert peak value to RMS value
    
    Converts a peak value to its RMS (Root Mean Square) equivalent 
    for sinusoidal waveforms.
    
    Args:
        peak_value: Peak value of the waveform
    
    Returns:
        RMS value of the waveform
    
    Formula:
        rms_value = peak_value / sqrt(2)
    
    Examples:
        >>> peak2rms(331.3)  # 331.3 V peak = 234 V RMS
        234.0
        >>> peak2rms(14.14)  # 14.14 A peak = 10 A RMS
        10.0
    
    """
    # For sinusoidal waveforms: RMS = Peak / √2
    return peak_value / math.sqrt(2)


def rms2peak(rms_value):
    """rms2peak Convert RMS value to peak value
    
    Converts an RMS (Root Mean Square) value to its peak equivalent 
    for sinusoidal waveforms.
    
    Args:
        rms_value: RMS value of the waveform
    
    Returns:
        Peak value of the waveform
    
    Formula:
        peak_value = rms_value * sqrt(2)
    
    Examples:
        >>> rms2peak(234)    # 234 V RMS = 331.3 V peak
        331.3
        >>> rms2peak(10)     # 10 A RMS = 14.14 A peak
        14.14
    
    """
    # For sinusoidal waveforms: Peak = RMS * √2
    return rms_value * math.sqrt(2)


def rpm2rads(rpm):
    """rpm2rads Convert RPM to radians per second
    
    Converts rotational speed from revolutions per minute (RPM) 
    to radians per second (rad/s).
    
    Args:
        rpm: Rotational speed in revolutions per minute
    
    Returns:
        Rotational speed in radians per second
    
    Formula:
        rads = rpm * (2π / 60)
    
    Examples:
        >>> rpm2rads(1800)  # 1800 RPM = 188.5 rad/s
        188.5
    
    """
    # Convert RPM to rad/s: 1 revolution = 2π radians, 1 minute = 60 seconds
    return rpm * (2 * math.pi / 60)


def rads2rpm(rads):
    """rads2rpm Convert radians per second to RPM
    
    Converts rotational speed from radians per second (rad/s) 
    to revolutions per minute (RPM).
    
    Args:
        rads: Rotational speed in radians per second
    
    Returns:
        Rotational speed in revolutions per minute
    
    Formula:
        rpm = rads * (60 / 2π)
    
    Examples:
        >>> rads2rpm(188.5)  # 188.5 rad/s = 1800 RPM
        1800.0
    
    """
    # Convert rad/s to RPM: 1 revolution = 2π radians, 1 minute = 60 seconds
    return rads * (60 / (2 * math.pi))

