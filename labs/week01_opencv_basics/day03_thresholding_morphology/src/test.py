from common_todo import find_input_images_todo,read_image_todo,to_grayscale_todo,save_image_todo
import common_todo

images=find_input_images_todo()

for image in images:
    image_name=image.stem
    print(image_name)
    


    image_object=read_image_todo(image) 
    
    print(f'{type(image_object)}--{image_object.dtype}--{image_object.shape}')
    
    
    print('------흑백변환------')
    
    
    gray_image=to_grayscale_todo(image_object)
    print(f'{type(gray_image)}--{gray_image.dtype}--{gray_image.shape}')
    
    gray_image_name=image_name+'_gray.png'
    print(gray_image_name)
    
    save_image_todo(common_todo.OUTPUT_IMAGE_DIR,gray_image_name,gray_image)
    
    