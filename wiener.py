import cv2
import numpy as np
from matplotlib import pyplot as plt

def wiener_filter(blurred_image, psf, noise_power_spectrum):
    # Fourier transform of the blurred image
    f_blurred = np.fft.fft2(blurred_image)

    # Fourier transform of the point spread function (PSF)
    f_psf = np.fft.fft2(psf, s=f_blurred.shape)

    # Power spectrum of the signal
    signal_power_spectrum = np.abs(f_psf) ** 2

    # Wiener filter formula
    wiener_filter = np.conj(f_psf) / (np.abs(f_psf) ** 2 + noise_power_spectrum / signal_power_spectrum)

    # Apply the Wiener filter
    f_restored = f_blurred * wiener_filter

    # Inverse Fourier transform to get the restored image
    restored_image = np.fft.ifft2(f_restored).real

    return restored_image

# Example usage
# Load the blurred image and the point spread function (PSF)
blurred_image = cv2.imread('image.jpeg', cv2.IMREAD_GRAYSCALE)
psf = np.ones((5, 5)) / 25.0  # Example PSF (5x5 averaging filter)

# Simulate noise (adjust the level based on your scenario)
noise_power_spectrum = 1e-3

# Apply Wiener filter
restored_image = wiener_filter(blurred_image, psf, noise_power_spectrum)

# Display the results
plt.subplot(1, 3, 1), plt.imshow(blurred_image, cmap='gray'), plt.title('Blurred Image')
plt.subplot(1, 3, 2), plt.imshow(restored_image, cmap='gray'), plt.title('Restored Image (Wiener Filter)')
plt.subplot(1, 3, 3), plt.imshow(np.abs(f_restored), cmap='gray'), plt.title('Filter Spectrum')
plt.show()
