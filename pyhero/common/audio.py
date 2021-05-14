import pyaudio

def print_audio_devices():
    """A quick helper method to see what PyAudio devices are available."""
    audio = pyaudio.PyAudio()
    cnt = audio.get_host_api_count()
    print ('Audio Drivers Available.')
    print ('idx out in name')
    for i in range(cnt):
        api = audio.get_host_api_info_by_index(i)
        print(f"{i:>2}: {api['defaultOutputDevice']:<3} {api['defaultInputDevice']:<2} {api['name']}")

    print ('\nAudio Devices Available.')
    print ('idx sample_rate out_channels out_latency in_channels in_latency name')
    cnt = audio.get_device_count()
    for i in range(cnt):
        dev = audio.get_device_info_by_index(i)
        print (
            f"{i:>2}: {dev['defaultSampleRate']:>11} {dev['maxOutputChannels']:>12} {dev['defaultHighOutputLatency']:>11}"\
            f"{dev['maxInputChannels']:>12} {dev['defaultHighInputLatency']:>10} {dev['name']}"
            )
    audio.terminate()

if __name__ == "__main__":
    print_audio_devices()
