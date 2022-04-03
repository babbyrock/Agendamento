import { AccountService } from '../../services/Account/account.service';
import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { UserLogin } from 'src/app/models/UserLogin';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  isPasswordVisible: Boolean = false;
  isConfirmPasswordVisible: Boolean = false;

  model =  {} as UserLogin;

  form!: FormGroup;

  constructor(private accountService: AccountService,
              private router: Router,
              private toaster: ToastrService) { }

  ngOnInit(): void {
  }

  redirectCreateAccount(){
    this.router.navigate(['criar-conta']);
  }

  next(){

  }

  handleIsPasswordVisible() {
    this.isPasswordVisible = !this.isPasswordVisible;
  }
  handleIsConfirmPasswordVisible() {
    this.isConfirmPasswordVisible = !this.isConfirmPasswordVisible;
  }

  login(): void{
    this.accountService.login(this.model).subscribe(
      () => { console.log("logou");},
      (error: any) => {
        if(error.status == 401)
          this.toaster.error('usuário ou senha inválidos');
        else console.error(error);
      }
     )
  }

}
