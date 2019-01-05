# darc-experiments-python

**Status:  🔥 Under active development. This is pre-alpha code. 🔥**

This code relates to the following pre-print. But, the pre-print is likely to appear in quite a different form when finally published.
> Vincent, B. T., & Rainforth, T. (2017, October 20). The DARC Toolbox: automated, flexible, and efficient delayed and risky choice experiments using Bayesian adaptive design. Retrieved from psyarxiv.com/yehjb


# What does this do?
The aim is to be able to run experiments using Bayesian Adaptive Design, using the approach set out in [Vincent & Rainforth, 2017](https://psyarxiv.com/yehjb). This was originally implemented in Matlab code in the [darc-experiments-matlab](https://github.com/drbenvincent/darc-experiments-matlab) repo, but I am porting this to Python.

Further, we are embedding this Bayesian Adaptive Design code within the [PsychoPy](http://www.psychopy.org) experiment framework.


# Features

## Core features
Feature | Status | Info
--- | --- | ---
Run DARC experiments in PsychoPy | ✅ | Run experiments with ease using PsychoPy
Exporting of data | ✅ | Exports raw trial-level data, summary statistics of our posteriors over model parameters, and a full particle-based representation of our posterior distribution over parameters. Reaction times are also exported.
Pick your own experiment design + model combination| ✅ | At this point we rely on very minor changes to the PsychoPy code snippets to select model and design preferences. (We might be able to explore doing this with a simple GUI in the future)
Customisable experimental protocol | ✅ | Easy to customise the set of allowable rewards, delays and probabilities, i.e. the design space. Make simple updates to Python code snippets in the PsychoPy Builder view.
Customise the framing of choices presented to participants. | ✅ | You can customise the way in which the experiment designs (rewards, delays, and probabilities) are presented to the participant by: a) altering stimulus components in the PsychoPy Builder view, and b) making edits to the short Python code snippets in PsychoPy

## Additional or advanced features
Feature | Status | Info
--- | --- | ---
Customise your prior beliefs over parameters | ✅ | This is a key feature of running efficient adaptive experiments. At the moment you have to edit priors in our Python code.
Basic results visualization | ✅ | So far we've got basic visualisation of the marginal posteriors over parameters, and also some basic plotting of the (design, response) data collected.
Run simulated experiments | ✅ | This is primarily used for code testing during development, but could also be useful to people wanting to conduct parameter recovery simulations on new models they develop.
Simultaneously fit mulitple models | ✅ | This is detailed in an example notebook. Currently it is an advanced feature without a PsychoPy demo.
Inject custom trials | ❌ | Left to it's own devices, an experiment will choose it's own set of designs. But if you have particular experimental needs, you can inject your own (manually specified) designs amongst automatically run trials.

## Customise your adaptive experiment for your purposes: choosing a design + model combination
When you run an adaptive experiment, it can be viewed as a combination of a **design paradigm** and a **cognitive model**. The design paradigm is essentially the space of possible designs (prospects presented to participants), and our Bayesian Adaptive Design methods select which to present to participants on a trial-to-trial basis, in real time. The goal of this is to maximise the information we gain about our model parameters.

So the experimenter must choose a design paradigm + cognitive model combination which will suit their purposes. This is actually a pretty straight-forward task. Your reasearch goals will dictate your design paradigm (eg delayed choice). You can use a default cognitive model (such as Hyperbolic discounting) or one of the other delay discounting models which you might be particularly interested in.

# Design paradigms
One of the core components of this package is to provide designs chosen through Bayesian Adaptive Design, as outlined in our prepint (Vincent & Rainforth, 2017). The core classes of design we focus on are:

- **Delayed choice tasks (aka inter-temporal choice):** you can choose between various protocols such as: front-end delays, fixed delayed reward, fixed immediate reward, fixed delay, etc.
- **Risky choice tasks:** Ahoose your range of reward probabilities. These can also be seen as a transformed version of odds against recieving a reward.
- **Simultaneous delayed and risky choice tasks:** Again, you can customise the range of delays and reward probability (risk) levels used in your experiment.

You can run experiments using any of the following design protocols:

Model | Type | Reference
--- | --- | ---
Kirby2009 | delayed | Kirby, K. N. (2009). One-year temporal stability of delay-discount rates. Psychonomic Bulletin & Review, 16(3):457–462.
Koffarnus_Bickel | delayed | Koffarnus, M. N., & Bickel, W. K. (2014). A 5-trial adjusting delay discounting task: Accurate discount rates in less than one minute. Experimental and Clinical Psychopharmacology, 22(3), 222-228.
Frye | delayed | Frye, C. C. J., Galizio, A., Friedel, J. E., DeHart, W. B., & Odum, A. L. (2016). Measuring Delay Discounting in Humans Using an Adjusting Amount Task. Journal of Visualized Experiments, (107), 1-8.
Griskevicius2011 | delayed or risky | Kirby, K. N. (2009). Griskevicius, V., Tybur, J. M., Delton, A. W., & Robertson, T. E. (2011). The influence of mortality and socioeconomic status on risk and delayed rewards: A life history theory approach. Journal of Personality and Social Psychology, 100(6), 1015–26.
DuGreenMyerson2002 | delayed or risky | Du, W., Green, L., & Myerson, J. (2002). Cross-cultural comparisons of discounting delayed and probabilistic rewards. The Psychological Record.
BayesianAdaptiveDesignGeneratorDARC | delayed and/or risky | Vincent & Rainforth (2017)

Below, we outline the cognitive models which we have implemented, for each of these classes of paradigms.

# DARC Cognitive models available

Yes, you can in run adaptive experiments to make very efficient inferences about the parameters for models of your choice 🙂 See below for a list of completed and planned model implementations.

## Delayed reward paradigm models
Model | Status | Info
--- | --- | ---
Exponential | ✅ | Samuelson, P. A. (1937). A note on measurement of utility. The Review of Economic Studies, 4(2), 155. http://doi.org/10.2307/2967612
Hyperbolic | ✅ | Mazur, J. E. (1987). An adjusting procedure for studying delayed reinforcement. In M. L. Commons, J. A. Nevin, & H. Rachlin (Eds.), Quantitative Analyses of Behavior (pp. 55–73). Hillsdale, NJ: Erlbaum.
HyperbolicMagnitudeEffect | ✅ | Vincent, B. T. (2016). Hierarchical Bayesian estimation and hypothesis testing for delay discounting tasks. Behavior Research Methods, 48(4), 1608–1620. http://doi.org/10.3758/s13428-015-0672-2
ExponentialMagnitudeEffect | ✅ |
ConstantSensitivity | ❌ | * Negative b values causing errors *
HyperbolicNonLinearUtility | ❌ | Cheng, J., & González-Vallejo, C. (2014). Hyperbolic Discounting: Value and Time Processes of Substance Abusers and Non-Clinical Individuals in Intertemporal Choice. PLoS ONE, 9(11), e111378–18. http://doi.org/10.1371/journal.pone.0111378
ExponentialPower | ❌ | Takahashi, T., Oono, H., and Radford, M. H. B. (2008). Psychophysics of time perception and intertemporal choice models. 387(8-9):2066–2074.
Rachlin hyperboloid | ❌ will not implement. See Modified Rachlin hyperboloid | Rachlin, H. (2006). Notes on Discounting. Journal of the experimental analysis of behavior, 85(3):425–435.
Modified Rachlin hyperboloid | ✅ | Vincent, B. T., & Stewart, N. (2018, October 16). The case of muddled units in temporal discounting. https://doi.org/10.31234/osf.io/29sgd
Myerson hyperboloid | ✅ | Myerson, J. and Green, L. (1995). Discounting of delayed rewards: Models of individual choice. Journal of the experimental analysis of behavior, 64(3):263–276.

## Risky reward paradigm models
Model | Status | Info
--- | --- | ---
Hyperbolic | ✅ | Hyperbolic discounting of odds against reward
Generalized hyperbolic | ❌ |
Prelec (1998) | ❌ |
Linear in log odds | ✅  | Gonzalez, R., & Wu, G. (1999). On the shape of the probability weighting function. Cognitive Psychology, 38(1), 129–166. http://doi.org/10.1006/cogp.1998.0710
Prospect Theory | ❌ |
Proportional difference | ✅ | González-Vallejo, C. (2002). Making trade-offs: A probabilistic and context-sensitive model of choice behavior. Psychological Review, 109(1), 137–155. http://doi.org/10.1037//0033-295X.109.1.137

## Delayed and risky reward paradigm models
Model | Status | Info
--- | --- | ---
AdditiveHyperbolic | ❌ | Yi, R., la Piedad, de, X., & Bickel, W. K. (2006). The combined effects of delay and probability in discounting. Behavioural Processes, 73(2), 149–155. http://doi.org/10.1016/j.beproc.2006.05.001
MultiplicativeHyperbolic | ✅ | Vanderveldt, A., Green, L., & Myerson, J. (2015). Discounting of monetary rewards that are both delayed and probabilistic: delay and probability combine multiplicatively, not additively. Journal of Experimental Psychology: Learning, Memory, and Cognition, 41(1), 148–162. http://doi.org/10.1037/xlm0000029
Probability and Time Trade-off model | ❌ | (Baucells & Heukamp)


# Installation instructions
1. Ensure you have a Python 3 installation. I recommend https://www.anaconda.com/download/. I have been testing the code with Python 3.6.6.
2. Install [PsychoPy](http://www.psychopy.org). Make sure you install a version that works with Python 3. Early development was done with PsychoPy 1.90.1, but it works just fine with [PsychoPy 3.0.0](https://github.com/psychopy/psychopy/releases/tag/3.0.0), so I recommend using that.
3. Download or clone this `darc-experiments-python` repository.
4. Open up PsychoPy... Open the PsychoPy experiment `psychopy/demo/experiment.psyexp` in the builder view... Run the experiment (with the green man symbol). You will get some GUI options to chose from before the experiment starts. After it is finished, check the auto-saved data in the `\data` folder. This includes log files, saved trial-level data, and exported figures which could be useful.


# How to...

(coming soon)


# Other packages/projects we rely upon

- [PsychoPy](http://www.psychopy.org) as the main experiment environment

Various Python packages such as:
- Numpy
- Pandas
- SciPy.stats. We use the scipy distributions to represent our prior beliefs over model parameters, and to draw samples from those prior beliefs. See [the full list of distributions here](https://docs.scipy.org/doc/scipy/reference/stats.html)


# References

**NOTE:** This work is based on the pre-print below. This is not yet published and is likely to appear in a subtantially altered form.

> Vincent, B. T., & Rainforth, T. (2017, October 20). The DARC Toolbox: automated, flexible, and efficient delayed and risky choice experiments using Bayesian adaptive design. Retrieved from [psyarxiv.com/yehjb](https://psyarxiv.com/yehjb)
