import numpy as np

def make_sin_wave(A, f, fs, sec):
  n = np.arange(0, fs*sec) / fs
  return A * np.sin(2 * np.pi * f * n)

def hamming(N: int): 
  n = np.arange(N)
  return 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

if __name__ == "__main__":
  import matplotlib.pyplot as plt
  from q03 import stft
  
  L = 1000
  S = 500
  sec = 0.1
  freq = 440
  fs = 16000
  x = make_sin_wave(1, freq, fs, sec)
  w = hamming(L)

  fl = stft(L, S, w, x)
  F = fl.shape[0]
  T = fl.shape[1]

  t = (np.arange(T) + 0.5) * sec / T
  f = np.arange(F) / F * fs / 2

  A = 20*np.log10(np.abs(fl))
  ang = np.angle(fl)

  fig, ax = plt.subplots(1, 2)

  ax[0].pcolormesh(t, f, A)
  ax[0].set_ylabel('Frequency [Hz]')
  ax[0].set_xlabel('Time [sec]')

  ax[1].pcolormesh(t, f, ang)
  ax[1].set_ylabel('Frequency [Hz]')
  ax[1].set_xlabel('Time [sec]')

  # fig.colorbar(orientation="vertical")
  plt.grid()
  plt.savefig('skotsugi/chapter04/q04.png')
