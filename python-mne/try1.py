from mayavi import mlab
import os.path as op
import mne
from mne.channels.montage import get_builtin_montages
from mne.datasets import fetch_fsaverage
from mne.viz import plot_alignment

subjects_dir = op.dirname(fetch_fsaverage())

for current_montage in get_builtin_montages():

    montage = mne.channels.read_montage(current_montage,
                                        unit='auto',
                                        transform=False)

    info = mne.create_info(ch_names=montage.ch_names,
                           sfreq=1,
                           ch_types='eeg',
                           montage=montage)

    fig = plot_alignment(info, trans=None,
                         subject='fsaverage',
                         subjects_dir=subjects_dir,
                         eeg=['projected'],
                         )
    mlab.view(135, 80)
    mlab.title(montage.kind, figure=fig)