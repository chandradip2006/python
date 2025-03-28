import random

print("Let's play Hangman!!")
chance=6
print(f"You have only {chance} lives so try to guess the word within {chance} attempts! Good luck")

words=['video', 'major', 'panic', 'fling', 'north', 'drive', 'fault', 'start', 'steak', 'laser', 'ivory', 'death', 'youth', 'short', 'eagle', 'grave', 'image', 'shout', 'order', 'sweat','aback', 'abase', 'abate', 'abbey', 'abbot', 'abhor', 'abide', 'abled', 'abode', 'abort', 'about', 'above', 'abuse', 'abyss', 'acorn', 'acrid', 'actor', 'acute', 'adage', 'adapt', 'adept', 'admin', 'admit', 'adobe', 'adopt', 'adore', 'adorn', 'adult', 'affix', 'afire', 'afoot', 'afoul', 'after', 'again', 'agape', 'agate', 'agent', 'agile', 'aging', 'aglow', 'agony', 'agree', 'ahead', 'aider', 'aisle', 'alarm', 'album', 'alert', 'algae', 'alibi', 'alien', 'align', 'alike', 'alive', 'allay', 'alley', 'allot', 'allow', 'alloy', 'aloft', 'alone', 'along', 'aloof', 'aloud', 'alpha', 'altar', 'alter', 'amass', 'amaze', 'amber', 'amble', 'amend', 'amiss', 'amity', 'among', 'ample', 'amply', 'amuse', 'angel', 'anger', 'angle', 'angry', 'angst', 'anime', 'ankle', 'annex', 'annoy', 'annual', 'anode', 'antic', 'anvil', 'aorta', 'apart', 'aphid', 'aping', 'apnea', 'apple', 'apply', 'apron', 'arbor', 'ardor', 'arena', 'argue', 'arise', 'armor', 'aroma', 'arose', 'array', 'arrow', 'arson', 'artsy', 'ascot', 'ashen', 'aside', 'askew', 'assay', 'asset', 'atoll', 'atone', 'attic', 'audio', 'audit', 'avail', 'avert', 'avian', 'avoid', 'await', 'awake', 'award', 'aware', 'awful', 'awing', 'axiom', 'azure', 'bacon', 'badge', 'badly', 'bagel', 'baggy', 'baker', 'baler', 'balls', 'balmy', 'bane', 'bangs', 'banjo', 'baron', 'basal', 'basic', 'basil', 'basin', 'basis', 'baste', 'batch', 'baton', 'batty', 'bawdy', 'bayou', 'beach', 'beady', 'beard', 'beast', 'beech', 'beefy', 'befit', 'began', 'begat', 'beget', 'begin', 'begun', 'being', 'belch', 'belie', 'belle', 'belly', 'below', 'bench', 'beret', 'berry', 'berth', 'beset', 'betel', 'bevel', 'bezel', 'bible', 'bicep', 'biddy', 'bigot', 'bilge', 'bingo', 'biome', 'birch', 'birth', 'bison', 'bitty', 'black', 'blade', 'blame', 'bland', 'blank', 'blare', 'blast', 'blaze', 'bleak', 'bleat', 'bleed', 'bleep', 'blend', 'bless', 'blimp', 'blind', 'blink', 'bliss', 'blitz', 'bloat', 'block', 'bloke', 'blond', 'blood', 'bloom', 'blown', 'bluer', 'bluff', 'blunt', 'blurb', 'blurt', 'blush', 'board', 'boast', 'bobby', 'boney', 'bongo', 'bonus', 'booby', 'boost', 'booth', 'booty', 'booze', 'boozy', 'borax', 'borne', 'bosom', 'bossy', 'botch', 'bough', 'boule', 'bound', 'bowel', 'boxer', 'brace', 'braid', 'brain', 'brake', 'brand', 'brash', 'brass', 'brave', 'bravo', 'brawl', 'brawn', 'bread', 'break', 'breed', 'briar', 'bribe', 'brick', 'bride', 'brief', 'brine', 'brink', 'brisk', 'broad', 'broil', 'broke', 'brood', 'brook', 'broom', 'broth', 'brown', 'brunt', 'brush', 'brute', 'buddy', 'budge', 'buggy', 'bugle', 'build', 'built', 'bulge', 'bulky', 'bully', 'bunch', 'bunny', 'burly', 'burnt', 'burst', 'bused', 'bushy', 'butch', 'butte', 'buxom', 'buyer', 'bylaw', 'cabal', 'cabin', 'cable', 'cacao', 'cache', 'cacti', 'cadet', 'cagey', 'cairn', 'camel', 'cameo', 'canal', 'candy', 'canny', 'canoe', 'canon', 'caper', 'caput', 'carat', 'cargo', 'carol', 'carry', 'carve', 'caste', 'catch', 'cater', 'catty', 'caulk', 'cause', 'cavil', 'cease', 'cedar', 'cello', 'chafe', 'chaff', 'chain', 'chair', 'chalk', 'champ', 'chant', 'chaos', 'chard', 'charm', 'chart', 'chase', 'chasm', 'cheap', 'cheat', 'check', 'cheek', 'cheer', 'chess', 'chest', 'chick', 'chide', 'chief', 'child', 'chili', 'chill', 'chime', 'china', 'chirp', 'chock', 'choir', 'choke', 'chord', 'chore', 'chose', 'chuck', 'chump', 'chunk', 'churn', 'chute', 'cider', 'cigar', 'cinch', 'circa', 'civic', 'civil', 'clack', 'claim', 'clamp', 'clang', 'clank', 'clash', 'clasp', 'class', 'clean', 'clear', 'cleat', 'cleft', 'clerk', 'click', 'cliff', 'climb', 'cling', 'clink', 'cloak', 'clock', 'clone', 'close', 'cloth', 'cloud', 'clout', 'clove', 'clown', 'cluck', 'clued', 'clumsy', 'clung', 'coach', 'coast', 'cobra', 'cocoa', 'colon', 'color', 'comet', 'comfy', 'comic', 'comma', 'conch', 'conda', 'coney', 'conic', 'copse', 'coral', 'corer', 'corny', 'couch', 'cough', 'could', 'count', 'coupe', 'court', 'coven', 'cover', 'covet', 'cower', 'coyly', 'crack', 'craft', 'cramp', 'crane', 'crank', 'crash', 'crass', 'crate', 'crave', 'crawl', 'craze', 'crazy', 'creak', 'cream', 'credo', 'creed', 'creek', 'creep', 'creme', 'crepe', 'crept', 'cress', 'crest', 'crick', 'cried', 'crier', 'crime', 'crimp', 'crisp', 'croak', 'crock', 'crone', 'crony', 'crook', 'cross', 'croup', 'crowd', 'crown', 'crude', 'cruel', 'crumb', 'crush', 'crust', 'crypt', 'cubic', 'cumin', 'curio', 'curly', 'curry', 'curse', 'curve', 'curvy', 'cutie', 'cyber', 'cycle', 'cynic', 'daddy', 'daily', 'dairy', 'daisy', 'dally', 'dance', 'dandy', 'datum', 'daunt', 'dealt', 'death', 'debar', 'debit', 'debug', 'debut', 'decal', 'decay', 'decor', 'decoy', 'decry', 'defer', 'deign', 'deity', 'delay', 'delta', 'delve', 'demon', 'denim', 'dense', 'depot', 'depth', 'derby', 'deter', 'detox', 'deuce', 'devil', 'diary', 'dicey', 'digit', 'dilly', 'dimly', 'diner', 'dirty', 'disco', 'ditch', 'ditto', 'ditty', 'diver', 'dizzy', 'dodgy', 'dogma', 'doing', 'dolla', 'dolly', 'donor', 'donut', 'dopey', 'doubt', 'dough', 'dowdy', 'dowel', 'downy', 'dowry', 'dozen', 'draft', 'drain', 'drake', 'drama', 'drank', 'drape', 'drawl', 'drawn', 'dread', 'dream', 'dress', 'dried', 'drier', 'drift', 'drill', 'drink', 'drive', 'droit', 'droll', 'drone', 'drool', 'droop', 'dross', 'drove', 'drown', 'druid', 'drunk', 'dryer', 'dryly', 'ducky', 'dully', 'dummy', 'dumpy', 'dunce', 'dusky', 'dusty', 'dutch', 'duvet', 'dwarf', 'dwell', 'dwelt', 'eager', 'eagle', 'early', 'earth', 'easel', 'eaten', 'eater', 'ebony', 'eclat', 'edict', 'edify', 'eerie', 'egret', 'eight', 'eject', 'eking', 'elate', 'elbow', 'elder', 'elect', 'elegy', 'elfin', 'elite', 'elope', 'elude', 'email', 'embed', 'ember', 'emcee', 'empty', 'enact', 'endow', 'enema', 'enemy', 'enjoy', 'ennui', 'ensue', 'enter', 'entry', 'envoy', 'epoch', 'epoxy', 'equal', 'equip', 'erase', 'erect', 'erode', 'error', 'erupt', 'essay', 'ester', 'ether', 'ethic', 'ethos', 'etude', 'evade', 'event', 'every', 'evict', 'evoke', 'exact', 'exalt', 'excel', 'exert', 'exile', 'exist', 'exit', 'expel', 'extol', 'extra', 'exult', 'eying', 'fable', 'facet', 'faint', 'fairy', 'faith', 'false', 'fancy', 'fanny', 'farce', 'fatal', 'fatly', 'fault', 'fauna', 'favor', 'feast', 'feats', 'fecal', 'feign', 'fella', 'felon', 'femme', 'fence', 'feral', 'ferry', 'fetal', 'fetch', 'fetid', 'fetus', 'fever', 'fewer', 'fiber', 'ficus', 'field', 'fiend', 'fiery', 'fifth', 'fifty', 'fight', 'filer', 'filet', 'filly', 'filmy', 'filth', 'final', 'finch', 'finer', 'first', 'fishy', 'fixer', 'fizzy', 'flack', 'flail', 'flair', 'flake', 'flaky', 'flame', 'flank', 'flare', 'flash', 'flask', 'fleck', 'fleet', 'flesh', 'flick', 'flier', 'fling', 'flint', 'flirt', 'float', 'flock', 'flood', 'floor', 'flour', 'flout', 'flour', 'flower', 'flown', 'fluff', 'fluid', 'fluke', 'flume', 'flung', 'flurry', 'flush', 'flute', 'flyer', 'foamy', 'focal', 'focus', 'foggy', 'foist', 'folio', 'folly', 'foray', 'force', 'forte', 'forth', 'forty', 'forum', 'found', 'foyer', 'frail', 'frame', 'frank', 'fraud', 'freak', 'freed', 'freer', 'fresh', 'friar', 'fried', 'frill', 'fringe', 'frisk', 'fritz', 'frock', 'frog', 'front', 'frost', 'froth', 'frown', 'froze', 'fruit', 'fudge', 'fugue', 'fully', 'fumbl', 'fungi', 'funky', 'funny', 'furor', 'furry', 'fussy', 'fuzzy', 'gaffe', 'gaily', 'gamer', 'gamma', 'gamut', 'gassy', 'gaudy', 'gauge', 'gaunt', 'gauze', 'gavel', 'gawky', 'gayer', 'gayly', 'gazer', 'gecko', 'geeky', 'geese', 'genie', 'genre', 'ghost', 'ghoul', 'giant', 'giddy', 'gipsy', 'girly', 'girth', 'given', 'giver', 'glade', 'gland', 'glare', 'glass', 'glaze', 'gleam', 'glean', 'glide', 'glint', 'gloat', 'globe', 'gloom', 'glory', 'gloss', 'glove', 'glowy', 'gluey', 'gnarl', 'gnome', 'godly', 'going', 'golem', 'golly', 'gonad', 'goner', 'goody', 'gooey', 'goofy', 'goose', 'gorge', 'gourd', 'grace', 'grade', 'graft', 'grail', 'grain', 'grand', 'grant', 'grape', 'graph', 'grasp', 'grass', 'grate', 'grave', 'gravy', 'graze', 'great', 'greed', 'green', 'greet', 'grief', 'grill', 'grind', 'gripe', 'groan', 'groin', 'groom', 'grope', 'gross', 'group', 'grout', 'grove', 'growl', 'grown', 'gruel', 'gruff', 'grunt', 'guard', 'guava', 'guess', 'guest', 'guide', 'guild', 'guile', 'guilt', 'guise', 'gulch', 'gully', 'gumbo', 'gummy', 'guppy', 'gusty', 'gypsy', 'habit', 'hairy', 'halve', 'handy', 'happy', 'hard', 'hasty', 'hatch', 'hater', 'haunt', 'haute', 'haven', 'havoc', 'hazel', 'heady', 'heard', 'heart', 'heavy', 'hedge', 'hefty', 'heist', 'helix', 'hello', 'hence', 'heron', 'hilly', 'hinge', 'hippo', 'hitch', 'hoard', 'hobby', 'hoist', 'holly', 'homer', 'honey', 'honor', 'horde', 'horny', 'horse', 'hotel', 'hound', 'house', 'hovel', 'hover', 'howdy', 'human', 'humid', 'humor', 'humph', 'humus', 'hunch', 'hunky', 'hunt', 'hurly', 'hurry', 'husky', 'hussy', 'hutch', 'hydro', 'hyena', 'hymen', 'hyper', 'icily', 'icing', 'ideal', 'idiom', 'idiot', 'igloo', 'iliac', 'image', 'imbue', 'impel', 'imply', 'inane', 'inbox', 'incur', 'index', 'inept', 'inert', 'infer', 'ingot', 'inlay', 'inlet', 'inner', 'input', 'inter', 'intro', 'ionic', 'irate', 'irony', 'islet', 'issue', 'itchy', 'ivory', 'jaunt', 'jazzy', 'jelly', 'jerky', 'jetty', 'jewel', 'jiffy', 'joint', 'joist', 'joker', 'jolly', 'joust', 'judge', 'juice', 'juicy', 'jumbo', 'jumpy', 'junta', 'junto', 'juror', 'kappa', 'karma', 'kayak', 'kebab', 'khaki', 'kinky', 'kiosk', 'kitty', 'knack', 'knave', 'knead', 'kneed', 'kneel', 'knelt', 'knife', 'knock', 'knoll', 'known', 'koala', 'krill', 'label', 'labor', 'laden', 'ladle', 'lager', 'laird', 'laity', 'lanky', 'lapel', 'lapse', 'large', 'larva', 'lasso', 'latch', 'later', 'lathe', 'latte', 'laugh', 'layer', 'leach', 'leafy', 'leaky', 'leant', 'leapt', 'learn', 'lease', 'leash', 'least', 'leave', 'ledge', 'leech', 'leery', 'lefty', 'legal', 'leggy', 'lemon', 'lemur', 'leper', 'level', 'lever', 'libel', 'liege', 'light', 'liken', 'lilac', 'limbo', 'limit', 'linen', 'liner', 'lingo', 'lipid', 'lithe', 'liver', 'livid', 'llama', 'loamy', 'loath', 'lobby', 'local', 'locus', 'lodge', 'lofty', 'logic', 'login', 'loopy', 'loose', 'lorry', 'loser', 'louse', 'lousy', 'lover', 'lower', 'lowly', 'loyal', 'lucid', 'lucky', 'lumen', 'lumpy', 'lunar', 'lunch', 'lunge', 'lupus', 'lurch', 'lurid', 'lusty', 'lying', 'lymph', 'lynch', 'lyric', 'macaw', 'macho', 'macro', 'madam', 'madly', 'mafia', 'magic', 'magma', 'maize', 'major', 'maker', 'mambo', 'mamma', 'mammy', 'manga', 'mange', 'mango', 'mania', 'manly', 'manor', 'maple', 'march', 'marry', 'marsh', 'mason', 'masse', 'match', 'matey', 'mauve', 'maxim', 'maybe', 'mayor', 'mealy', 'meant', 'meaty', 'mecca', 'medal', 'media', 'medic', 'melee', 'melon', 'mercy', 'merge', 'merit', 'merry', 'metal', 'meter', 'metro', 'micro', 'midge', 'midst', 'might', 'milky', 'mimic', 'mince', 'miner', 'minim', 'minor', 'minty', 'minus', 'mirth', 'miser', 'missy', 'mocha', 'modal', 'model', 'modem', 'mogul', 'moist', 'molar', 'moldy', 'money', 'month', 'moody', 'moose', 'moral', 'moron', 'morph', 'mossy', 'motel', 'motif', 'motor', 'motto', 'moult', 'mound', 'mount', 'mourn', 'mouse', 'mouth', 'mover', 'movie', 'mower', 'much', 'mucky', 'mucus', 'muddy', 'mulch', 'mummy', 'munch', 'mural', 'murky', 'mushy', 'music', 'musky', 'musty', 'mylar', 'myrrh', 'nadir', 'naive', 'nanny', 'nasal', 'nasty', 'natal', 'naval', 'navel', 'needy', 'neigh', 'nerdy', 'nerve', 'never', 'newer', 'newly', 'nicer', 'niche', 'niece', 'night', 'ninja', 'ninth', 'noble', 'nobly', 'noise', 'noisy', 'nomad', 'noose', 'north', 'nose', 'noted', 'novel', 'nudge', 'nurse', 'nutty', 'nylon', 'nymph', 'oaken', 'obese', 'occur', 'ocean', 'octal', 'octet', 'odder', 'oddly', 'offal', 'offer', 'often', 'olden', 'older', 'olive', 'ombre', 'omega', 'onion', 'onset', 'opera', 'opine', 'opium', 'optic', 'orbit', 'order', 'organ', 'other', 'otter', 'ought', 'ounce', 'outdo', 'outer', 'outgo', 'ovate', 'overt', 'ovine', 'ovoid', 'owing', 'owner', 'oxide', 'ozone', 'paddy', 'pagan', 'paint', 'paler', 'palsy', 'panel', 'panic', 'pansy', 'papal', 'paper', 'parer', 'parka', 'parry', 'parse', 'party', 'pasta', 'paste', 'pasty', 'patch', 'patio', 'patty', 'pause', 'payee', 'payer', 'peace', 'peach', 'pearl', 'pecan', 'pedal', 'penal', 'pence', 'penne', 'penny', 'perch', 'peril', 'perky', 'pesky', 'pesto', 'petal', 'petty', 'phase', 'phone', 'phony', 'photo', 'piano', 'picky', 'piece', 'piety', 'piggy', 'pilot', 'pinch', 'piney', 'pinky', 'pinto', 'piper', 'pique', 'pitch', 'pithy', 'pivot', 'pixel', 'pixie', 'pizza', 'place', 'plaid', 'plain', 'plait', 'plane', 'plank', 'plant', 'plate', 'plaza', 'plead', 'pleat', 'plied', 'plier', 'pluck', 'plumb', 'plume', 'plump', 'plunk', 'plush', 'poesy', 'point', 'poise', 'poker', 'polar', 'polka', 'polyp', 'pooch', 'poppy', 'porch', 'poser', 'posit', 'posse', 'pouch', 'pound', 'pouty', 'power', 'prank', 'prawn', 'press', 'price', 'prick', 'pride', 'pried', 'prime', 'primo', 'print', 'prior', 'prism', 'privy', 'prize', 'probe', 'prone', 'prong', 'proof', 'prose', 'proud', 'prove', 'prowl', 'proxy', 'prude', 'prune', 'psalm', 'pubic', 'pudgy', 'puffy', 'pulpy', 'pulse', 'punch', 'pupal', 'pupil', 'puppy', 'puree', 'purer', 'purge', 'purse', 'pushy', 'putty', 'pygmy', 'quack', 'quail', 'quake', 'qualm', 'quark', 'quart', 'quash', 'quasi', 'queen', 'queer', 'quell', 'query', 'quest', 'queue', 'quick', 'quiet', 'quill', 'quilt', 'quirk', 'quit', 'quiver', 'quoth', 'rabbi', 'rabid', 'racer', 'radar', 'radii', 'raged', 'raggy', 'rainy', 'raise', 'rajah', 'rally', 'ramen', 'ranch', 'randy', 'range', 'rapid', 'rarer', 'raspy', 'ratio', 'ratty', 'raven', 'rayon', 'razor', 'reach', 'react', 'ready', 'realm', 'rearm', 'rebel', 'rebus', 'rebut', 'recap', 'recur', 'recut', 'reedy', 'refer', 'refit', 'regal', 'rehab', 'reign', 'relax', 'relay', 'relic', 'remit', 'renal', 'renew', 'repay', 'repel', 'reply', 'rerun', 'reset', 'resin', 'retch', 'retro', 'retry', 'reuse', 'revel', 'revue', 'rhino', 'rhyme', 'rider', 'ridge', 'rifle', 'right', 'rigid', 'rigor', 'rinse', 'ripen', 'risen', 'riser', 'risky', 'rival', 'river', 'roach', 'roast', 'robin', 'robot', 'rocky', 'rodeo', 'roger', 'rogue', 'roomy', 'roost', 'rotor', 'rouge', 'rough', 'round', 'rouse', 'route', 'rover', 'rowdy', 'rower', 'royal', 'ruddy', 'ruder', 'rugby', 'ruler', 'rumba', 'rumor', 'rupee', 'rural', 'rusty', 'sadly', 'safer', 'saint', 'salad', 'sally', 'salon', 'salsa', 'salty', 'samey', 'sandy' , 'zebra' , 'zesty']

# words=words.split(" ")
# print(words)


# print(f"list of words: {words}")
word = random.choice(words)
word1=word
# count=len(word) 
count=5
# print("You have total 6 chances")
print(f"Word length: {count}")
list=['_' , '_' , '_' , '_' , '_']
while True:
    print(list)
    char = input("guess a letter: ")
    if char in word:
        print("good guess")
        list[word.find(char)]=char
        word=word.replace(char,"-" , 1)
        count=count-1
        if count==0:
            word=word.replace(char,"-" , 1)
            print(list)
            print(f"congratulations you won!!!")
            break
        print(f"life remaining: {chance}")
    else :
        # print("wrong guess , try again")
        print(f"You guessed {char} that is not present in the word  . So you lose a life")
        chance=chance-1
        if chance==0:
            print(f"game over  , you die , the word was {word1}")
            break
        print(f"life remaining: {chance}")
