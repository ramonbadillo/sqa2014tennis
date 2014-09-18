# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m



@step(u'Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def given_group1_and_group2_start_a_match_to_group3_sets(step, jugador1,
														 jugador2, sets):
    world.match = m.Match(jugador1, jugador2, sets)


@step(u'Then: I see score: "([^"]*)"')
def then_i_see_score_group1(step, score):
    assert world.match.score_set() == score, \
        "Got %s" % world.match.score_set()


@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_group1_won_the_group2_set_group3_group4(step, jugador1, 
													numeroset, puntojugador1, 
													puntojugador2):
    world.match.save_set_won(jugador1)
    world.match.save_score_set(puntojugador1,
                               puntojugador2,
                               numeroset,
                               jugador1)


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_group1_won_the_group2_set_group3_group4(step, jugador1, 
													numeroset, puntojugador1, 
													puntojugador2):
    world.match.save_set_won(jugador1)
    world.match.save_score_set(puntojugador1,
                               puntojugador2,
                               numeroset,
                               jugador1)


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is_group1(step, score):
    assert world.match.score_set() == score, \
        "Got %s" % world.match.score_set()
