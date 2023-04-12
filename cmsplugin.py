from abc import ABC, abstractmethod

class MyCMSPlugin(ABC):
	@abstractmethod
	def get_config(self):
	    pass
    
    @abstractmethod
	def render(self):
		pass


class ImageGalleryPlugin(MyCMSPlugin):
	def get_config(self):
	    return {
        	'image_folder': '/path/to/images',
        	'max_images': 10
    	}
	
    def render(self):
    	# Render the image gallery on a webpage
    	pass

