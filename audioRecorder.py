import pyaudiowpatch as pyaudio
import local_statistics as lStat

CHANNELS = 1
CHUNK_SIZE = 1024
HOP_LENGTH = CHUNK_SIZE // 2
SHORT_NORMALIZE = (1.0 / 32768.0)
FORMAT = pyaudio.paFloat32

class ARException(Exception):
    """Base class for AudioRecorder`s exceptions"""
class WASAPINotFound(ARException):
    ...
class InvalidDevice(ARException):
    ...

class AudioRecorder:

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = None

    def get_sample_size(self, data_format=FORMAT):
        return self.p.get_sample_size(data_format)

    def get_default_wasapi_device(self):

        try: # Get default WASAPI info
            wasapi_info = self.p.get_host_api_info_by_type(pyaudio.paWASAPI)
        except OSError:
            raise WASAPINotFound("Looks like WASAPI is not available on the system")
        
        sys_default_speakers = self.p.get_device_info_by_index(wasapi_info['defaultOutputDevice'])

        if not sys_default_speakers['isLoopbackDevice']:
            for loopback in self.p.get_loopback_device_info_generator():
                if sys_default_speakers['name'] in loopback['name']:
                    return loopback
                    
            else:
                raise InvalidDevice('Default loopback ouput device not found.\n\nRun "python -m pyaudiowpatch" to check available devices.')
    
    def start_recording(self, target_device:dict):
        self.close_stream()

        self.stream = self.p.open(format=FORMAT,
                                  channels=1,
                                  rate=int(target_device['defaultSampleRate']),
                                  frames_per_buffer=CHUNK_SIZE,
                                  input=True,
                                  input_device_index=target_device['index'])

    def stop_stream(self):
        self.stream.stop_stream()
        
    def start_stream(self):
        self.stream.start_stream()
    
    def close_stream(self):        
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

    
def convert_audio(data, min_range=-1, max_range=1, rounded=0):
    '''Convert audio data to median value'''
    result = lStat.normalisation_samples(data, min_range=min_range, max_range=max_range, rounded=rounded)
    result = lStat.median(result, rounded=rounded)
    return result


