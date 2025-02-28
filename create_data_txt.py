import os
import random

# Function to split data and create train.txt and val.txt
def split_data_and_generate_txt(image_folder, train_txt, val_txt, train_ratio=0.8):
    # Get list of all image files in the folder
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

    # Shuffle the image list to randomize the split
    random.shuffle(image_files)

    # Calculate the number of training and validation samples
    total_images = len(image_files)
    num_train = int(total_images * train_ratio)
    num_val = total_images - num_train

    # Split the images into train and val sets
    train_images = image_files[:num_train]
    val_images = image_files[num_train:]

    # Write the file names with their suffixes into train.txt and val.txt
    with open(train_txt, 'w') as train_file:
        for image in train_images:
            train_file.write(image + '\n')  # Write each image name with its suffix

    with open(val_txt, 'w') as val_file:
        for image in val_images:
            val_file.write(image + '\n')  # Write each image name with its suffix

    print(f"Training data saved to {train_txt} with {num_train} images.")
    print(f"Validation data saved to {val_txt} with {num_val} images.")

# Example usage
image_folder = r"D:\arshad\latent diff\arbitrary-scale-diffusion\data\CT\single slice COVID19 CT Data"  # Replace with your image folder path
train_txt = r'D:\arshad\latent diff\arbitrary-scale-diffusion\data\CT\single slice COVID19 CT Data\train.txt'  # Output file for training data
val_txt = r'D:\arshad\latent diff\arbitrary-scale-diffusion\data\CT\single slice COVID19 CT Data\val.txt'      # Output file for validation data

# Call the function to split the data and generate the txt files
split_data_and_generate_txt(image_folder, train_txt, val_txt)
