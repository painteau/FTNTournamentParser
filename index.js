const { readFile, writeFile } = require('fs').promises;
const parse = require('replay-reader');
 
(async () => {
  const replayBuffer = await readFile('./Replays/season08-2019.04.05.replay');
  const parsedReplay = parse(replayBuffer);
  await writeFile('./parsedReplay.json', JSON.stringify(parsedReplay, null, 2));
  console.log('Wrote results to ./parsedReplay.json');
})();