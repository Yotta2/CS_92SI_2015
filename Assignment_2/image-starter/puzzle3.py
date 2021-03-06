import sys
from image import load_image, save_image, show_image, show_all_images, files_in_directory

def calc_pixels_similarity(pixel0, pixel1):
	"""
	Calculate the similarity of two pixels, which is defined as
	square of the absolute difference between each color channel.
	"""
	similarity = 0
	for i in range(len(pixel0)):
		diff = pixel0[i] - pixel1[i]
		similarity += diff * diff
	return similarity

def calc_slices_similarity(slices, left, right):
	"""
	Calculate the similarity of two slices.
	"""
	similarity = 0
	# m is width
	left_slice_m = len(slices[left])
	for i in range(len(slices[left][0])):
		left_pixel = slices[left][left_slice_m - 1][i]
		right_pixel = slices[right][0][i]
		similarity += calc_pixels_similarity(left_pixel, right_pixel)
	return similarity

def findBestMatch(slices):
	"""
	Find the best match with slice0 in the given slices.
	Best match is defined as two slices with min sum of 
	squares of the absolute difference between each color channel.
	Return a tuple of (index_of_left_slice, index_of_right_slice)
	"""
	left_index = 0
	right_index = 0
	best_similarity = sys.maxsize

	for i in range(1, len(slices)):
		# slice 0 is left slice, slice i is right slice
		similarity = calc_slices_similarity(slices, 0, i)
		if similarity < best_similarity:
			left_index, right_index, best_similarity = 0, i, similarity
		# slice i is left slice, slice 0 is right slice
		similarity = calc_slices_similarity(slices, i, 0)
		if similarity < best_similarity:
			left_index, right_index, best_similarity = i, 0, similarity
		#print("best_similarity: {0}".format(best_similarity))
	return left_index, right_index

def merge(slices, left_index, right_index):
	"""
	Merge two slices.
	"""
	slices[left_index] = slices[left_index] + slices[right_index]
	slices.pop(right_index)

def main():
	images_dir = input("Please enter the directory containing the shredded images to be reassembled: ")
	filenames = files_in_directory(images_dir)
	print("files to be reassembled: {0}".format(filenames))
	slices = []
	for filename in filenames:
		slices.append(load_image(filename))
	#show_all_images(slices[0], tuple(slices[1:]))
	while len(slices) > 1:
		left_index, right_index = findBestMatch(slices)
		print((left_index, right_index))
		merge(slices, left_index, right_index)
	show_image(slices[0])

if __name__ == '__main__':
    """This block is run if and only if the Python script is invoked from the
    command line."""
    main()