# Extract running time and memory usage info from GNU time output


import glob


def extract_timing_and_memory(filename):
	with(open(filename, 'r')) as infile:
		line = ''
		while line.strip() != 'time result':  # skip tool's stdout
			line = infile.readline()
		infile.readline()  # skip line with command
		wall_time = float(infile.readline().strip().split(' ')[-1][:-1])  # extracted from this format: "real 4501.63s"
		user_time = float(infile.readline().strip().split(' ')[-1][:-1])  # extracted from this format: "user 4501.63s"
		sys_time = float(infile.readline().strip().split(' ')[-1][:-1])  # extracted from this format: "sys 4501.63s"
		wall_time = wall_time / 3600.0  # convert seconds to hours
		cpu_time = (user_time + sys_time) / 3600.0  # CPU time = User time + Sys time; convert seconds to hours
		memory = float(infile.readline().strip().split(':')[1][:-2])  # from this format: "memory:39261932KB"
		memory = memory / 1000.0 / 1000.0  # convert from KB to GB
	return wall_time, cpu_time, memory


def get_total_runtime_and_max_mem(all_fnames):
	wall_times, cpu_times, memory_usages = [], [], []
	for fname in all_fnames:
		wall, cpu, mem = extract_timing_and_memory(fname)
		wall_times.append(wall)
		cpu_times.append(cpu)
		memory_usages.append(mem)
	return [str(sum(wall_times)), str(sum(cpu_times)), str(max(memory_usages))]


metalign_timing_files = glob.glob('cami_timing/timing_metalign_*.txt')
metalign_data = get_total_runtime_and_max_mem(metalign_timing_files)
#
kraken2_timing_files = glob.glob('cami_timing/timing_kraken2_*.txt')
kraken2_data = get_total_runtime_and_max_mem(kraken2_timing_files)
#
clark_timing_files = glob.glob('cami_timing/timing_clark_*.txt')
clark_data = get_total_runtime_and_max_mem(clark_timing_files)
#
gottcha_timing_files = glob.glob('cami_timing/timing_gottcha_*.txt')
gottcha_data = get_total_runtime_and_max_mem(gottcha_timing_files)
#
megan_timing_files = glob.glob('cami_timing/timing_*megan*.txt')
megan_data = get_total_runtime_and_max_mem(megan_timing_files)
#
metabing2_timing_files = glob.glob('cami_timing/timing_metabing2_*.txt')
metabing2_data = get_total_runtime_and_max_mem(metabing2_timing_files)
#
metaphlan2_timing_files = glob.glob('cami_timing/timing_metaphlan_*.txt')
metaphlan2_data = get_total_runtime_and_max_mem(metaphlan2_timing_files)
#
motus2_timing_files = glob.glob('cami_timing/timing_motus2_*.txt')
motus2_data = get_total_runtime_and_max_mem(motus2_timing_files)

# write in a tabbed format that can easily be read by pandas in the plotting script
outname = 'plot_inputs/cami_timing_memory.txt'
with(open(outname, 'w')) as outfile:
	outfile.write('\tWallclock time\tCPU time\tMax Memory Usage (GB)\n')
	outfile.write('Metalign\t' + '\t'.join(metalign_data) + '\n')
	outfile.write('Kraken2\t' + '\t'.join(kraken2_data) + '\n')
	outfile.write('CLARK\t' + '\t'.join(clark_data) + '\n')
	outfile.write('GOTTCHA\t' + '\t'.join(gottcha_data) + '\n')
	outfile.write('MEGAN+DIAMOND\t' + '\t'.join(megan_data) + '\n')
	outfile.write('MetaBinG2\t' + '\t'.join(metabing2_data) + '\n')
	outfile.write('MetaPhlAn2\t' + '\t'.join(metaphlan2_data) + '\n')
	outfile.write('mOTUS2\t' + '\t'.join(motus2_data) + '\n')

# Now get real data timing
metalign_peabody = get_total_runtime_and_max_mem(['peabody_timing/timing_metalign.txt'])
metalign_tara_small = get_total_runtime_and_max_mem(['tara_timing/timing_metalign_ERR598952_interleaved.txt'])
metalign_tara_large = get_total_runtime_and_max_mem(['tara_timing/timing_metalign_ERR598957_interleaved.txt'])
#
kraken2_peabody = get_total_runtime_and_max_mem(['peabody_timing/timing_kraken2_fastq_version.txt'])
kraken2_tara_small = get_total_runtime_and_max_mem(['tara_timing/timing_kraken2__ERR598952_interleaved.txt'])
kraken2_tara_large = get_total_runtime_and_max_mem(['tara_timing/timing_kraken2__ERR598957_interleaved.txt'])
#
clark_peabody = get_total_runtime_and_max_mem(['peabody_timing/timing_clark_fastq_version.txt'])
clark_tara_small = get_total_runtime_and_max_mem(['tara_timing/timing_clark_ERR598952_interleaved.txt'])
clark_tara_large = get_total_runtime_and_max_mem(['tara_timing/timing_clark_ERR598957_interleaved.txt'])
#
gottcha_peabody = get_total_runtime_and_max_mem(['peabody_timing/timing_gottcha_fastq_version.txt'])
gottcha_tara_small = get_total_runtime_and_max_mem(['tara_timing/timing_gottcha_ERR598952_interleaved.txt'])
gottcha_tara_large = get_total_runtime_and_max_mem(['tara_timing/timing_gottcha_ERR598957_interleaved.txt'])
#
megan_peabody = get_total_runtime_and_max_mem(glob.glob('peabody_timing/*megan*'))
megan_tara_small = get_total_runtime_and_max_mem(glob.glob('tara_timing/*megan*'))
megan_tara_large = ['', '', '']  # timed out after a week
#
metabing2_peabody = get_total_runtime_and_max_mem(['peabody_timing/timing_metabing2_gpu_fasta_version.txt'])
metabing2_tara_small = get_total_runtime_and_max_mem(['tara_timing/timing_metabing2_gpu_ERR598952_interleaved.txt'])
metabing2_tara_large = get_total_runtime_and_max_mem(['tara_timing/timing_metabing2_gpu_ERR598957_interleaved.txt'])
#
metaphlan2_peabody = get_total_runtime_and_max_mem(['peabody_timing/timing_metaphlan_fastq_version.txt'])
metaphlan2_tara_small = get_total_runtime_and_max_mem(['tara_timing/timing_metaphlan_ERR598952_interleaved.txt'])
metaphlan2_tara_large = get_total_runtime_and_max_mem(['tara_timing/timing_metaphlan_ERR598957_interleaved.txt'])
#
motus2_peabody = get_total_runtime_and_max_mem(['peabody_timing/timing_motus2_fastq_version.txt'])
motus2_tara_small = get_total_runtime_and_max_mem(['tara_timing/timing_motus2_ERR598952_interleaved.txt'])
motus2_tara_large = get_total_runtime_and_max_mem(['tara_timing/timing_motus2_ERR598957_interleaved.txt'])
#

# write in a tabbed format that can easily be read by pandas in the plotting script
outname = 'plot_inputs/real_data_wallclock_time.txt'
metalign_wallclocks = [metalign_peabody[0], metalign_tara_small[0], metalign_tara_large[0]]
kraken2_wallclocks = [kraken2_peabody[0], kraken2_tara_small[0], kraken2_tara_large[0]]
clark_wallclocks = [clark_peabody[0], clark_tara_small[0], clark_tara_large[0]]
gottcha_wallclocks = [gottcha_peabody[0], gottcha_tara_small[0], gottcha_tara_large[0]]
megan_wallclocks = [megan_peabody[0], megan_tara_small[0], megan_tara_large[0]]
metabing2_wallclocks = [metabing2_peabody[0], metabing2_tara_small[0], metabing2_tara_large[0]]
metaphlan2_wallclocks = [metaphlan2_peabody[0], metaphlan2_tara_small[0], metaphlan2_tara_large[0]]
motus2_wallclocks = [motus2_peabody[0], motus2_tara_small[0], motus2_tara_large[0]]
with(open(outname, 'w')) as outfile:
	outfile.write('\t0.1\t11\t98\n')
	outfile.write('Metalign\t' + '\t'.join(metalign_wallclocks) + '\n')
	outfile.write('Kraken2\t' + '\t'.join(kraken2_wallclocks) + '\n')
	outfile.write('CLARK\t' + '\t'.join(clark_wallclocks) + '\n')
	outfile.write('GOTTCHA\t' + '\t'.join(gottcha_wallclocks) + '\n')
	outfile.write('MEGAN+DIAMOND\t' + '\t'.join(megan_wallclocks) + '\n')
	outfile.write('MetaBinG2\t' + '\t'.join(metabing2_wallclocks) + '\n')
	outfile.write('MetaPhlAn2\t' + '\t'.join(metaphlan2_wallclocks) + '\n')
	outfile.write('mOTUs2\t' + '\t'.join(motus2_wallclocks) + '\n')

# write in a tabbed format that can easily be read by pandas in the plotting script
outname = 'plot_inputs/real_data_cpu_time.txt'
metalign_cpu = [metalign_peabody[1], metalign_tara_small[1], metalign_tara_large[1]]
kraken2_cpu = [kraken2_peabody[1], kraken2_tara_small[1], kraken2_tara_large[1]]
clark_cpu = [clark_peabody[1], clark_tara_small[1], clark_tara_large[1]]
gottcha_cpu = [gottcha_peabody[1], gottcha_tara_small[1], gottcha_tara_large[1]]
megan_cpu = [megan_peabody[1], megan_tara_small[1], megan_tara_large[1]]
metabing2_cpu = [metabing2_peabody[1], metabing2_tara_small[1], metabing2_tara_large[1]]
metaphlan2_cpu = [metaphlan2_peabody[1], metaphlan2_tara_small[1], metaphlan2_tara_large[1]]
motus2_cpu = [motus2_peabody[1], motus2_tara_small[1], motus2_tara_large[1]]
with(open(outname, 'w')) as outfile:
	outfile.write('\t0.1\t11\t98\n')
	outfile.write('Metalign\t' + '\t'.join(metalign_cpu) + '\n')
	outfile.write('Kraken2\t' + '\t'.join(kraken2_cpu) + '\n')
	outfile.write('CLARK\t' + '\t'.join(clark_cpu) + '\n')
	outfile.write('GOTTCHA\t' + '\t'.join(gottcha_cpu) + '\n')
	outfile.write('MEGAN+DIAMOND\t' + '\t'.join(megan_cpu) + '\n')
	outfile.write('MetaBinG2\t' + '\t'.join(metabing2_cpu) + '\n')
	outfile.write('MetaPhlAn2\t' + '\t'.join(metaphlan2_cpu) + '\n')
	outfile.write('mOTUs2\t' + '\t'.join(motus2_cpu) + '\n')

# write in a tabbed format that can easily be read by pandas in the plotting script
outname = 'plot_inputs/real_data_memory.txt'
metalign_mem = [metalign_peabody[2], metalign_tara_small[2], metalign_tara_large[2]]
kraken2_mem = [kraken2_peabody[2], kraken2_tara_small[2], kraken2_tara_large[2]]
clark_mem = [clark_peabody[2], clark_tara_small[2], clark_tara_large[2]]
gottcha_mem = [gottcha_peabody[2], gottcha_tara_small[2], gottcha_tara_large[2]]
megan_mem = [megan_peabody[2], megan_tara_small[2], megan_tara_large[2]]
metabing2_mem = [metabing2_peabody[2], metabing2_tara_small[2], metabing2_tara_large[2]]
metaphlan2_mem = [metaphlan2_peabody[2], metaphlan2_tara_small[2], metaphlan2_tara_large[2]]
motus2_mem = [motus2_peabody[2], motus2_tara_small[2], motus2_tara_large[2]]
with(open(outname, 'w')) as outfile:
	outfile.write('\t0.1\t11\t98\n')
	outfile.write('Metalign\t' + '\t'.join(metalign_mem) + '\n')
	outfile.write('Kraken2\t' + '\t'.join(kraken2_mem) + '\n')
	outfile.write('CLARK\t' + '\t'.join(clark_mem) + '\n')
	outfile.write('GOTTCHA\t' + '\t'.join(gottcha_mem) + '\n')
	outfile.write('MEGAN+DIAMOND\t' + '\t'.join(megan_mem) + '\n')
	outfile.write('MetaBinG2\t' + '\t'.join(metabing2_mem) + '\n')
	outfile.write('MetaPhlAn2\t' + '\t'.join(metaphlan2_mem) + '\n')
	outfile.write('mOTUs2\t' + '\t'.join(motus2_mem) + '\n')

# get custom kraken2 timing and memory info
# [str(sum(wall_times)), str(sum(cpu_times)), str(max(memory_usages))]
with(open('cami_timing/custom_kraken2_all_timing.txt', 'r')) as infile:
	splits = infile.readline().strip().split()
	user_time = float(splits[0].split('user')[0])
	sys_time = float(splits[1].split('system')[0])
	cpu_time = (user_time + sys_time) / 3600.0
	elapsed = splits[2].split('elapsed')[0]
	elapsed_mins, elapsed_secs = [float(i) for i in elapsed.split(':')]
	wall_time = ((elapsed_mins * 60.0) + elapsed_secs) / 3600.0
	max_mem = float(splits[-1].split('maxresident')[0]) / 1000.0 / 1000.0
	custom_data = [str(wall_time), str(cpu_time), str(max_mem)]

# write timing and memory info for custom kraken2 experiment
# write in a tabbed format that can easily be read by pandas in the plotting script
outname = 'plot_inputs/custom_timing_memory.txt'
with(open(outname, 'w')) as outfile:
	outfile.write('\tWallclock time\tCPU time\tMax Memory Usage (GB)\n')
	outfile.write('Metalign\t' + '\t'.join(metalign_data) + '\n')
	outfile.write('Kraken2_original\t' + '\t'.join(kraken2_data) + '\n')
	outfile.write('Kraken2_custom\t' + '\t'.join(custom_data) + '\n')
#

# Metalign / MEGAN+DIAMOND Multithreading time scaling experiment
metalign_4threads = get_total_runtime_and_max_mem(['cami_timing/timing_metalign_5mil_reads_4threads_RL_S001.txt'])
metalign_8threads = get_total_runtime_and_max_mem(['cami_timing/timing_metalign_5mil_reads_8threads_RL_S001.txt'])
metalign_16threads = get_total_runtime_and_max_mem(['cami_timing/timing_metalign_5mil_reads_16threads_RL_S001.txt'])
metalign_32threads = get_total_runtime_and_max_mem(['cami_timing/timing_metalign_5mil_reads_32threads_RL_S001.txt'])
#
megan_4threads = get_total_runtime_and_max_mem(['cami_timing/timing_diamond_5mil_reads_4threads_RL_S001.txt',
													'cami_timing/timing_meganize_5mil_reads_4threads_RL_S001.txt'])
megan_8threads = get_total_runtime_and_max_mem(['cami_timing/timing_diamond_5mil_reads_8threads_RL_S001.txt',
													'cami_timing/timing_meganize_5mil_reads_8threads_RL_S001.txt'])
megan_16threads = get_total_runtime_and_max_mem(['cami_timing/timing_diamond_5mil_reads_16threads_RL_S001.txt',
													'cami_timing/timing_meganize_5mil_reads_16threads_RL_S001.txt'])
megan_32threads = get_total_runtime_and_max_mem(['cami_timing/timing_diamond_5mil_reads_32threads_RL_S001.txt',
													'cami_timing/timing_meganize_5mil_reads_32threads_RL_S001.txt'])
#

# write in a tabbed format that can easily be read by pandas in the plotting script
outname = 'plot_inputs/thread_scaling_wallclock_time.txt'
metalign_thread_wallclocks = [metalign_4threads[0], metalign_8threads[0], metalign_16threads[0], metalign_32threads[0]]
megan_thread_wallclocks = [megan_4threads[0], megan_8threads[0], megan_16threads[0], megan_32threads[0]]
with(open(outname, 'w')) as outfile:
	outfile.write('\t4\t8\t16\t32\n')
	outfile.write('Metalign\t' + '\t'.join(metalign_thread_wallclocks) + '\n')
	outfile.write('MEGAN+DIAMOND\t' + '\t'.join(megan_thread_wallclocks) + '\n')

# write in a tabbed format that can easily be read by pandas in the plotting script
outname = 'plot_inputs/thread_scaling_cpu_time.txt'
metalign_thread_cpu = [metalign_4threads[1], metalign_8threads[1], metalign_16threads[1], metalign_32threads[1]]
megan_thread_cpu = [megan_4threads[1], megan_8threads[1], megan_16threads[1], megan_32threads[1]]
with(open(outname, 'w')) as outfile:
	outfile.write('\t4\t8\t16\t32\n')
	outfile.write('Metalign\t' + '\t'.join(metalign_thread_cpu) + '\n')
	outfile.write('MEGAN+DIAMOND\t' + '\t'.join(megan_thread_cpu) + '\n')
