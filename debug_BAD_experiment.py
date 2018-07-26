from darc.delayed import models
from darc.designs import Kirby2009, Frye, DARC_Designs
import random

design_thing = DARC_Designs()
model = models.Hyperbolic(n_particles=5_000)

for trial in range(15):
    design = design_thing.get_next_design(model)

    # make up a random resonse and enter it
    if random.random() < 0.5:
        last_response_chose_B = True
    else:
        last_response_chose_B = False

    design_thing.enter_trial_design_and_response(
        design, last_response_chose_B)

    # update beliefs
    model.update_beliefs(design_thing.all_data)

    print(f'trial {trial} complete 🙂')

print('Simulated BAD experiment complete: 😀 ✅')

model.export_posterior_histograms('bzz')
design_thing.plot_all_data('bzz')
