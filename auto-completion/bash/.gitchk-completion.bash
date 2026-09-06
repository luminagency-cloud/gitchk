
_gitchk_completions()
{

  local cur commands repos cmd
  local IFS=$'\n\t '

  cur=${COMP_WORDS[COMP_CWORD]}
  cmd=${COMP_WORDS[1]}


  # this doesn't work for two repos with the same basename
  #gitchk_path=${XDG_CONFIG_HOME:-$HOME/.config}/gitchk/repo_path
  #repos=`awk '{split($0, paths, ":")} END {for (i in paths) {n=split(paths[i],b, /\//); print b[n]}}' ${gitchk_path}`

  if [ $COMP_CWORD -eq 1 ]; then
    # FIXME: this is somewhat slow
    commands=`gitchk -h | sed '2q;d' |sed 's/[{}.,]/ /g'`
    COMPREPLY=($(compgen -W "${commands}" ${cur}))
  elif [ $COMP_CWORD -gt 1 ]; then
    case $cmd in
      add)
        COMPREPLY=($(compgen -d ${cur}))
        ;;
      clone)
        COMPREPLY=($(compgen -f ${cur}))
        ;;
      color | flags)
        COMPREPLY=($(compgen -W "ll set" ${cur}))
        ;;
      ll | context)
        groups=`gitchk group ls`
        COMPREPLY=($(compgen -W "${groups}" ${cur}))
        return
        ;;
      *)
        repos=`gitchk ls`
        COMPREPLY=($(compgen -W "${repos}" ${cur}))
        ;;
    esac
  fi
}

complete -F _gitchk_completions gitchk

